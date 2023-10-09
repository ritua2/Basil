import os
import yaml

# Returns a dictionary containing the data
def parse_commands(filepath):

    with open(filepath, "r") as ff:
        return yaml.safe_load(ff)

# Finds a list of all provided commands
# Requires the data in dictionary form
def provided_instructions(raw_data):

    valid_tags = ["Base", "Working directory", "Setup", "Contents", "Environment variables", "Default command", "Entry command", "Expose ports", "Volumes", "Advanced copy"]

    return [key for key in raw_data if key in valid_tags]

# Checks that, a minimum, the base exists
# If so, it returns [Dockerfile syntax, False]
# If error: [Error explained, True]
def base_check(raw_data):

    if "Base" not in raw_data:
        return ["INVALID: Base image was not selected", True]

    return [raw_data["Base"], False]

def image_check(raw_data):

    if "Image type" not in raw_data:
        return ["INVALID: Image type was not selected", True]

    return [raw_data["Image type"], False]

# Orders all inputs according to their order
def order_inputs(raw_data):

    tags_to_order = provided_instructions(raw_data)

    tags_to_order.remove("Base")
    if "Default command" in tags_to_order:
        tags_to_order.remove("Default command")
    if "Entry command" in tags_to_order:
        tags_to_order.remove("Entry command")

    all_tags = []

    for atype in tags_to_order:

        for numbered_order, instruction in raw_data[atype].items():
            all_tags.append([int(numbered_order), instruction, atype])

    # Sorts them by location
    all_tags.sort(key=lambda x: x[0])

    locs = [x[0] for x in all_tags ]

    # There cannot be two equally ordered commands
    if len(locs) != len(list(set(locs))):
        return ["INVALID: There cannot be two instructions with the same order priority", True]
    else:
        return [all_tags, False]

# From the list of all tags, it combines commands which are next to each other
# already_sorted_instructions (arr) [order (int), instruction (str), type (str)]
# Returns the list shortened and already sorted as before
def commands_combiner(already_sorted_instructions, spacing="    "):

    processed_commands = []
    for an_instruction in already_sorted_instructions:

        if an_instruction[2] == "Already completed":
            continue

        if an_instruction[2] != "Setup":
            processed_commands.append(an_instruction)
            continue

        successive_commands = [an_instruction[1]]
        current_location = already_sorted_instructions.index(an_instruction)

        for nvnv in range(current_location+1, len(already_sorted_instructions)):

            next_instruction = already_sorted_instructions[nvnv]

            if next_instruction[2] != "Setup":
                break

            # If this a command
            successive_commands.append(next_instruction[1])
            next_instruction[2] = "Already completed"

        an_instruction[1] = successive_commands

    return already_sorted_instructions

##############################################
# Processes a series of instructions for Docker
###############################################

# base image
def df_base(basename):
    return "FROM "+basename

# Working directory
def df_workdir(workdir):
    return "WORKDIR "+workdir

# Run commands
# run_comm (arr) (str): Contains several commands to provision the container
def df_run(run_comm, spacing="    "):
    return "\nRUN "+(" &&\\\n"+spacing).join(run_comm)

# Copies a file
# If the path is not specified, it is assumed to be in the current working directory of the container
def df_copy(copy_instruction):
    copy_broken = copy_instruction.split(":")
    if len(copy_broken) == 1:
        return "\nCOPY "+copy_broken[0]+" ."
    else:
        return "\nCOPY "+copy_broken[0]+" "+copy_broken[1]

# Adds an environmental variable
# If the path is not specified, it is assumed to be in the current working directory of the container
def df_env(envar_instruction):
    if isinstance(envar_instruction, dict):
       key, value = next(iter(envar_instruction.items()))
       return f"ENV {key}={value}"
    else:
       return f"ENV {envar_instruction}"
    #env_broken = envar_instruction.split(":")
    #return "ENV "+env_broken[0]+" "+env_broken[1]

# Prints the default command
def df_cmd(cmd_instruction):

    cmd_space_broken = cmd_instruction.split(" ")
    cmd_space_broken = ["\""+a+"\"" for a in cmd_space_broken if a != '']

    return "CMD [" + ", ".join(cmd_space_broken) + "]"

def df_ent(ent_instruction):
    ent_space_broken = ent_instruction.split(" ")
    ent_space_broken = ["\""+a+"\"" for a in ent_space_broken if a != '']
    return "ENTRYPOINT [" + ", ".join(ent_space_broken) + "]"

def df_expose(expose_instruction):
    return "EXPOSE "+ str(expose_instruction)

def df_volume(volume_instruction):
    return "VOLUME "+ str(volume_instruction)

def df_acopy(acopy_instruction):
    copy_broken = str(acopy_instruction).split("<::>")
    if len(copy_broken) == 2:
        return "ADD "+copy_broken[0]+" "+copy_broken[1]
    return ""

####################################################
# Processes a series of instructions for Singularity
####################################################

# bootstrap

# base image
def sf_base(basename):
    return "From: "+basename

# Run commands
# run_comm (arr) (str): Contains several commands to provision the container
def sf_run(run_comm, spacing="    "):
    return "\n%post\n    "+(" &&\\\n"+spacing).join(run_comm)

# Copies a file
# If the path is not specified, it is assumed to be in the current working directory of the container
def sf_copy(copy_instruction):
    #return "%files\n"+spacing+(copy_instruction)
    #return copy_instruction
    copy_broken = copy_instruction.split(":")
    return ""+copy_broken[0]+" "+copy_broken[1]

# Adds an environmental variable
# If the path is not specified, it is assumed to be in the current working directory of the container
def sf_env(envar_instruction):
    if isinstance(envar_instruction, dict):
       key, value = next(iter(envar_instruction.items()))
       return f"export {key}={value}"
    else:
       return f"export {envar_instruction}"
    #envar_instruction = envar_instruction.replace(":","=",1)
    #return "export "+ envar_instruction

# Prints the default command
def sf_cmd(cmd_instruction):
    cmd_space_broken = cmd_instruction.split(" ")
    cleaned_cmds = [cmd for cmd in cmd_space_broken if cmd != '']

    return "%runscript\n    " + " ".join(cleaned_cmds)

# Given all instructions, it processes them and writes them into a file
# dockerfile_path (str): path of the created Dockerfile
# image_base (str): image base
# default_comm (str): default command
# ordered_instructions (arr) [number, instruction, type]

# FOR DOCKER
def write_to_dockerfile(dockerfile_path, image_base, ordered_instructions, default_comm=False, entry_comm=False, spacing="    "):

        with open(dockerfile_path, "w") as dfp:
            dfp.write(df_base(image_base)+"\n\n")

            for an_instruction in ordered_instructions:

                if an_instruction[2] == "Working directory":
                    dfp.write(df_workdir(an_instruction[1])+"\n")
                elif an_instruction[2] == "Setup":
                    dfp.write(df_run(an_instruction[1], spacing)+"\n")
                elif an_instruction[2] == "Contents":
                    dfp.write(df_copy(an_instruction[1])+"\n")
                elif an_instruction[2] == "Environment variables":
                    dfp.write(df_env(an_instruction[1])+"\n")
                elif an_instruction[2] == "Expose ports":
                    dfp.write(df_expose(an_instruction[1])+"\n")
                elif an_instruction[2] == "Volumes":
                    dfp.write(df_volume(an_instruction[1])+"\n")
                elif an_instruction[2] == "Advanced copy":
                    dfp.write(df_acopy(an_instruction[1])+"\n")

            if entry_comm:
                    dfp.write("\n"+df_ent(entry_comm)+"\n")
            if default_comm:
                dfp.write("\n"+df_cmd(default_comm)+"\n")

# FOR SINGULARITY
def write_to_def_file(def_file_path, image_base, ordered_instructions, default_comm=False, entry_comm=False, spacing="    "):

    with open(def_file_path, "w") as dfp:
        #
        files_to_copy = []
        env_to_copy = []
        #
        dfp.write("Bootstrap: docker\n")
        dfp.write(sf_base(image_base)+"\n")

        for an_instruction in ordered_instructions:

            if an_instruction[2] == "Setup":
                dfp.write(sf_run(an_instruction[1], spacing)+"\n")
            elif an_instruction[2] == "Contents":
                files_to_copy.append(sf_copy(an_instruction[1]))
            elif an_instruction[2] == "Environment variables":
                env_to_copy.append(sf_env(an_instruction[1]))

        #
        if env_to_copy:
            dfp.write("\n%environment\n")
            for env_instruction in env_to_copy:
                dfp.write(spacing + env_instruction + "\n")

        if files_to_copy:
            dfp.write("\n%files\n")
            for file_instruction in files_to_copy:
                dfp.write(spacing + file_instruction + "\n")

        if default_comm:
            dfp.write("\n"+sf_cmd(default_comm)+"\n")

# Given a json/yaml file with the instructions, it creates the dockerfile
# file_with_data (str): path to the file to be parsed
def create_imagefile(file_with_data, output_file_path, spacing="    "):
    original_data = parse_commands(file_with_data)

    it = image_check(original_data)
    if it[1]:
        return it[0]

    image_type_check = it[0]

    bc = base_check(original_data)
    if bc[1]:
        return bc[0]
    image_base = bc[0]

    provided_inputs = order_inputs(original_data)
    if provided_inputs[1]:
        return provided_inputs[0]

    combined_inputs = commands_combiner(provided_inputs[0], spacing)

    if "Default command" not in original_data:
        original_data["Default command"] = False

    if image_type_check == 'docker':
        if output_file_path is None:
            output_file_path = "Dockerfile"
        write_to_dockerfile(output_file_path, image_base, combined_inputs, original_data.get("Default command",False), original_data.get("Entry command",False), spacing)
        return output_file_path
    elif image_type_check == 'singularity':
        if output_file_path is None:
            output_file_path = "singularity.def"
        write_to_def_file(output_file_path, image_base, combined_inputs, original_data.get("Default command",False), original_data.get("Entry command",False), spacing)
        return output_file_path
