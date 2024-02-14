#!/usr/bin/python
import os
import re
import sys

def input_(prompt):
    return input("\n" + prompt + "  ")

def print_(message):
    print()
    print("-" * 100)
    print("\n\n" + message + "\n")

def gather_input(prompt, collection=None):
    inputs = []
    while True:
        user_input = input(prompt)
        if not user_input:
            break
        if collection and user_input not in collection:
            print("Invalid input. Please select from the provided options.")
            continue
        inputs.append(user_input)
    return inputs


def create_basil_file(img_type = 'docker'):
    images_and_package_manager = [
        ("ubuntu:23.10", "apt"),
        ("ubuntu:kinetic", "apt"),
        ("ubuntu:focal", "apt"),
        ("ubuntu:mantic", "apt"),
        ("debian:stable", "apt"),
        ("debian:stable-slim", "apt"),
        ("debian:stable-backports", "apt"),
        ("node:20.5.0-slim","apt"),
        ("node:20.4-bookworm-slim", "apt"),
        ("node:20.3.1-slim", "apt"),
        ("postgres:16beta2-bullseye", "apt"),
        ("postgres:14", "apt"),
        ("nginx:1.21.6", "apt"),
        ("nginx:stable-perl", "apt"),
        ("nginx:1.25-perl", "apt"),
        ("nginx:mainline-perl", "apt"),
        ("python:3.12-rc", "apt"),
        ("python:3.12.0b4-slim-bullseye", "apt"),
        ("python:3.12.0b3-slim", "apt"),
        ("graphcore/tensorflow", "apt"),
        ("graphcore/tensorflow:2", "apt"),
        ("graphcore/pytorch:3.3.0-ubuntu-20.04-20230703", "apt"),
        ("graphcore/pytorch", "apt"),
        ("php", "apt"),
        ("php:fpm", "apt"),
        ("php:zts", "apt"),
        ("alpine:3.16.6", "apk"),
        ("alpine:edge", "apk"),
        ("centos:centos8", "yum"),
        ("centos:centos7", "yum"),
        ("centos:centos6", "yum"),
    ]

    print_("Available set of base images for BASIL: ")
    for index, image_and_pkg_manager in enumerate(images_and_package_manager, start=1):
        print(f"{index}. {image_and_pkg_manager[0]}")

    selection = input_(">>> Please select the base image by entering its number and make sure that you are inside the project folder that you uploaded: ")

    while not selection.isdigit() or not 1 <= int(selection) <= len(images_and_package_manager):
        print("INVALID SELECTION. PLEASE PROVIDE THE INPUT AGAIN.\n")
        selection = input_(">>> Please select the base image by entering its number: ")
    BASE_IMAGE, PKG_MANAGER = images_and_package_manager[int(selection) - 1]

    WORKDIR = ""
    if img_type == 'docker':
        WORKDIR = input_(">>> Enter work directory: [OPTIONAL]")

    ENV_VARIABLES = []
    # We will change this later to accept the variable names and values as pairs.
    print_(">>> Please enter the environment variables and their values. First enter the environment variable name. Then, you will be prompted for the environment variable value. Press ENTER to skip when you don't have anything more to enter.")
    while True:
        ENV_VAR = input_(f"[{len(ENV_VARIABLES)+1}]: VARIABLE NAME: ")
        if (ENV_VAR == ""):
            print()
            break
        ENV_VAR_VAL = input_(f"[{len(ENV_VARIABLES)+1}]: VARIABLE VALUE: ")

        confirmation = input_(f"Do you want to add `{ENV_VAR}={ENV_VAR_VAL}`? [Y/n]]\n")
        if confirmation.lower() != 'n':
            ENV_VARIABLES.append((ENV_VAR,ENV_VAR_VAL))

    CONTENTS = []
    print_(">>> Enter the relative filepaths (including the filenames) that you want to package in the image. Please note that the path should be relative to your current working directory or folder. Press ENTER to skip when you don't have anything more to enter. ")
    while True:
        CONTENT_SRC = input_(f"[{len(CONTENTS)+1}]: ENTER RELATIVE FILE PATH (THIS IS THE 'SOURCE' FOR THE COPY COMMAND): ")
        if(CONTENT_SRC==""):
            print()
            break

        CONTENT_DEST = input_(f"[{len(CONTENTS)+1}]: ENTER ABSOLUTE FILE PATH THAT SHOULD BE CREATED INSIDE THE IMAGE (THIS IS THE 'DESTINATION' FOR THE COPY COMMAND) ")

        confirmation = input_(f"Do you want to add '{CONTENT_SRC}' to '{CONTENT_DEST}'? [Y/n]\n")
        if confirmation.lower() != 'n':
            CONTENTS.append((CONTENT_SRC, CONTENT_DEST))

    ADVANCED_COPY = []
    if img_type == 'docker':
        print_(">>> ADVANCED COPY: Enter the names of the files that you want to package in the image. Press ENTER to skip when you don't have anything more to enter ...")
        note = """

            Advanced way to copy files to Docker image
            - Web File Downloads: Download files directly from the web and add them to your Docker images.
            - Flexible Copy Operations: Copy files and folders based on specific patterns to defined locations within your Docker images.
            - Simple Decompression: Easily decompress tar files without any manual effort.
            Examples:
                1. Web File Download:
                    source: https://example.com/sample-file.txt
                    destination: /path/to/destination/sample-file.txt

                2. Copy Files using wildcard characters which are matched using Go's filepath.Match rules. check this link for more details: https://pkg.go.dev/path/filepath#Match
                    source: myapp-*.js
                    destination: /app/

                3. Simplified Decompression of Tar Files:
                    source: myapp.tar.gz
                    destination: /destination/folder/
                
        """
        print(note)
        while True:
            CONTENT_SRC = input_(f"[{len(ADVANCED_COPY)+1}]: ENTER RELATIVE FILE PATH (THIS IS THE 'SOURCE' FOR THE COPY COMMAND): ")
            if(CONTENT_SRC==""):
                print()
                break

            CONTENT_DEST = input_(f"[{len(CONTENTS)+1}]: ENTER ABSOLUTE FILE PATH THAT SHOULD BE CREATED INSIDE THE DOCKER IMAGE (THIS IS THE 'DESTINATION' FOR THE COPY COMMAND): ")

            confirmation = input_(f"Do you want to add '{CONTENT_SRC}' to '{CONTENT_DEST}'? [Y/n]\n")
            if confirmation.lower() != 'n':
                ADVANCED_COPY.append((CONTENT_SRC, CONTENT_DEST))

    VOLUMES = []
    if img_type == 'docker':
        print_(">>> Enter the volumes that you want to mount with the docker image. Press ENTER to skip when you don't have anything more to enter ...")
        note = """
            Volumes will persist the data even after your execution of your Docker container. For example if you provide "/data", a data folder will be created in the root directory inside the Docker image and the data will persist in docker volumes even after the container terminates.
        """
        print(note)
        while True:
            VOLUME = input_(f"[{len(VOLUMES)+1}]: ")
            if(VOLUME==""):
                print()
                break
            confirmation = input_(f"Do you want to add volume '{VOLUME}'? [Y/n]\n")
            if confirmation.lower() != 'n':
                VOLUMES.append(VOLUME)

    EXPOSE_PORTS = []
    print_(">>> Enter the ports that you want to expose to the host name. Press ENTER to skip when you don't have anything more to enter ...")
    note = """
        For example if you provide "8080", the port 8080 will be exposed to the host machine and you can access the application running inside the container from your host machine.
    """
    print(note)
    while True:
        PORT = input_(f"[{len(EXPOSE_PORTS)+1}]: ")
        if(PORT==""):
            print()
            break
        confirmation = input_(f"Do you want to expose port '{PORT}'? [Y/n]\n")
        if confirmation.lower() != 'n':
            EXPOSE_PORTS.append(PORT)

    # Removing this as it is very confusing.
    # PACKAGES = []
    # print(">>> Enter any software packages or dependencies or prerequisites that are required to complete the installation. Press ENTER to skip when you don't have anything more to enter ...")
    # while True:
    #     PKG = input_(f"[{len(PACKAGES)+1}]: ")
    #     if(PKG==""):
    #         print()
    #         break
    #     confirmation = input_(f"Do you want to install '{PKG}'? [Y/n]\n")
    #     if confirmation.lower() != 'n':
    #         PACKAGES.append(PKG)

    SETUP_CMDS = []
    print_(">>> Enter the commands for building the code, including any commands required for running the prerequisite software packages. Press ENTER to skip when you don't have anything more to enter ...")

    while True:
        CMD = input_(f"[{len(SETUP_CMDS)+1}]: ")
        if (CMD == ""):
            print()
            break
        confirmation = input_(f"Do you want to add command `${CMD}` to setup your project environment? [Y/n]\n")
        if confirmation.lower() != 'n':
            SETUP_CMDS.append(CMD)
    
    ENTRYPOINT = ""
    if img_type == 'docker':
        print_(">>>  There is a notion of 'entry command' and a 'default command'. The 'entry command' is optional but if provided it is fixed and cannot be overridden at run-time. This command would be the first command that is run when your Docker image is run as a container. The 'default command' is also optional, but if provided, it is the default command that is run when the container runs, and this command will run after the 'entry command' is run. In case there is no 'entry command' provided, the 'default command' would be the first one to run. It should be noted that unlike the 'entry command', the 'default command', can be overridden at run-time by passing command-line arguments through the 'docker run' command. You can choose to provide an 'entry command' only, or a 'default command' only, or both 'entry command' and 'default command'. One scenario where 'entry command' and 'default command' are used together is when a command has a fixed-part, and a variable part that can change everytime the command is run. In this scenario, the fixed part of the command is added to the 'entry command' and the 'default command' is used as a place-holder or to pass default value to the 'entry command' with the understanding that the 'default command' can be overridden by passing command-line arguments at run-time using the 'docker run' command.")
        
        ENTRYPOINT = input_("Enter an 'entry command' that should be run every time the image is run as a container (optional). \n")
    

    DEFAULT_CMDS = []
    print_(">>> Enter commands that should run every time you run the image. Press ENTER to skip when you don't have anything more to enter ...")

    while True:
        CMD = input_(f"[{len(DEFAULT_CMDS)+1}]: ")
        if (CMD == ""):
            print()
            break
        confirmation = input_(f"Do you want to add command `${CMD}` to run when you run the image? [Y/n]\n")
        if confirmation.lower() != 'n':
            DEFAULT_CMDS.append(CMD)

    # list of valid licenses
    licenses = [
        ("AFL 2.0", "AFL-2.0.txt", []),
        ("AFL 2.1", "AFL-2.1.txt", []),
        ("AGPL 3.0 or later", "AGPL-3.0-or-later", ['name', 'year']),
        ("AGPL 3.0 only", "AGPL-3.0-only.txt", ['program info', 'year', 'name']),
        ("Apache 1.1", "Apache-1.1.txt", []),
        ("Apache 2.0", "Apache-2-0.txt", ['year', 'name']),
        ("Artistic 1.0 Perl", "Artistic-1.0-Perl", []),
        ("BSD-2-Clause-Patent", "BSD-2-Clause-Patent.txt", ['year', 'copyright holder']),
        ("BSD-2-Clause", "BSD-2-Clause.txt", ['year', 'owner']),
        ("BSD-3-Clause", "BSD-3-Clause.txt", ['year', 'owner']),
        ("BSD-4-Clause-UC", "BSD-4-Clause-UC.txt", []),
        ("BSD-4-Clause", "BSD-4-Clause.txt", ['year', 'owner']),
        ("BSL 1.0", "BSL-1.0.txt", []),
        ("CDDL 1.0", "CDDL-1.0.txt", []),
        ("CPL 1.0", "CPL-1.0.txt", []),
        ("EFL 2.0", "EFL-1.0.txt", []),
        ("EPL 1.0", "EPL-1.0.txt", []),
        ("EPL 2.0", "EPL-1.0.txt", []),
        ("EUPL 1.1", "EUPL-1.1.txt", []),
        ("GPL 2.0", "GPL-2.0-only.txt", ['program info', 'year', 'name', 'signature', 'date', 'designation']),
        ("GPL 2.0 or later", "GPL-2.0-or-later.txt", ['program info', 'year', 'name', 'signature', 'date', 'designation']),
        ("GPL 3.0", "GPL-3.0-only.txt", ['program info', 'year', 'name']),
        ("GPL 3.0 or later", "GPL-3.0-or-later.txt", ['program info', 'year', 'name']),
        ("IPL 1.0", "IPL-1.0.txt", []),
        ("ISC", "ISC.txt", ['copyright notice']),
        ("LGPL 2.1 or later", "LGPL-2.1-or-later.txt", ['program info', 'year', 'name', 'signature', 'date', 'designation']),
        ("LGPL 2.1", "LGPL-2.1-only.txt", ['program info', 'year', 'name', 'signature', 'date', 'designation']),
        ("LGPL 3.0", "LGPL-3.0-only.txt", []),
        ("LGPL 3.0 or later", "LGPL-3.0-or-later.txt", []),
        ("LibPNG", "LibPNG.txt", []),
        ("MIT", "MIT.txt", ['year', 'copyright holder']),
        ("MPL 1.1", "MPL-1.1.txt", ['language type', 'name', 'year', 'owner']),
        ("MPL 2.0", "MPL-2.0.txt", []),
        ("NBPL 1.0", "NBPL-1.0.txt", []),
        ("OSL 3.0", "OSL-3.0.txt", []),
        ("RPL 1.5", "RPL-1.5.txt", []),
        ("UPL 1.0", "UPL-1.0.txt", []),
        ("Zlib", "Zlib.txt", ['year', 'copyright holder']),
    ]

    placeholders = {
            "name": "license_author_name",
            "year": "license_year",
            "owner": "license_owner",
            "language type": "license_language_type",
            "program info": "license_program_info",
            "designation": "license_designation",
            "date": "license_date",
            "signature": "license_signature",
            "copyright holder": "license_copyright_holder",
            "copyright notice": "license_copyright_notice"
        }
    """
                          <label for="name">Please enter the name of the individual/entity responsible for creating the software: </label>

                          <label for="year">Please enter the year of creation/publication of software: </label>

                          <label for="owner">Please enter the name of the individual/organization that legally owns the software: </label>

                          <label for="language_type">Please enter the programming language(s) used in the software: </label>

                          <label for="program_info">Please enter any important information/description regarding the software: </label>

                          <label for="designation">Please enter the role of the person representing the copyright holder: </label>

                          <label for="date">Please enter the date on which the license agreement was signed or comes into effect: </label>

                          <label for="signature">Please enter the name or initials of the copyright holder: </label>

                          <label for="copyright_notice">Please enter the statement that will be used to indicate that the software is protected by copyright law: </label>

                          <label for="copyright_holder">Please enter the name of the person/entity that owns the legal copyright for the software: </label>
    """
    placeholder_desc = {
        "name": "Please enter the name of the individual/entity responsible for creating the software: ",
        "year": "Please enter the year of creation/publication of software: ",
        "owner": "Please enter the name of the individual/organization that legally owns the software: ",
        "language type": "Please enter the programming language(s) used in the software: ",
        "program info": "Please enter any important information/description regarding the software: ",
        "designation": "Please enter the role of the person representing the copyright holder: ",
        "date": "Please enter the date on which the license agreement was signed or comes into effect: ",
        "signature": "Please enter the name or initials of the author: ",
        "copyright notice": "Please enter the statement that will be used to indicate that the software is protected by copyright law:",
        "copyright holder": "Please enter the name of the person/entity that owns the legal rights for the software: "
    }

    # provide list of licenses to choose from. Provide extra option in the last for no license.
    print_(">>> Select a license for your project. Select last option if you don't want to add any license.")
    for i, license in enumerate(licenses):
        print(f"[{i}]: {license[0]}")
    else:
        print(f"[{len(licenses)}]: No license")

    while True:
        try:
            license_number = int(input_(f"[1]: Enter the license number: "))
            if license_number == len(licenses):
                confirmation = input_("Are you sure you do not want to add a license? [Y/n]\n")
                if confirmation.lower() != 'n' and confirmation.lower() != 'no':
                    LICENSE = ""
                    break
                else:
                    continue

            LICENSE = licenses[license_number][1]

            confirmation = input_(f"Do you want to add license '{LICENSE}'? [Y/n]\n")
            if confirmation.strip().lower() != "n" and confirmation.strip().lower() != "no":
                for placeholder in licenses[license_number][2]:
                    placeholders[placeholder] = input_(placeholder_desc.get(placeholder, f"Please enter the {placeholder}: "))
                break
            else:
                continue

        except:
            print("Please enter a valid license number: ")
            continue
        
    if LICENSE != "":
        license_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../licenses")
        license_template_path = os.path.join(license_dir, LICENSE)

        # Read license template
        with open(license_template_path, 'r') as license_template:
            license_content = license_template.read()

        # Copy a license template to the current directory
        license_file_path = os.path.join(os.getcwd(), "LICENSE.txt")
        with open(license_file_path, 'w') as license_file:
            license_file.write(license_content)

        # Construct the regex pattern
        regex = r'{{%\s*(.*?)\s*%}}'

        pattern = re.compile(regex)
        modified_license_content = pattern.sub(lambda match: placeholders.get(match.group(1), match.group(0)), license_content)

        # Write modified license content to a file
        with open(license_file_path, 'w') as writer:
            writer.write(modified_license_content)

        CONTENTS.append(("LICENSE.txt", "LICENSE"))

    with open('midas.yml','w+') as midas_file:

        midas_file.write(f"Image type: '{img_type}'\n")

        # ADDING BASE IMAGE SO THAT THE YAML FILE IS VALID
        midas_file.write(f"Base: \"{BASE_IMAGE}\"\n")

        NUM = 1
        if WORKDIR != "":
            midas_file.write("Working directory:\n")
            midas_file.write(f' 1: "{WORKDIR}"\n')
            NUM+=1

        if len(ENV_VARIABLES) > 0:
            midas_file.write("Environment variables:\n")
            for _ in range(len(ENV_VARIABLES)):
                midas_file.write(f' {NUM}:\n')
                midas_file.write(f'  {ENV_VARIABLES[_][0]}:{ENV_VARIABLES[_][1]}\n')
                NUM += 1

        if len(CONTENTS) > 0:
            midas_file.write("Contents:\n")
            for _ in range(len(CONTENTS)):
                midas_file.write(f' {NUM}: "{CONTENTS[_][0]}:{CONTENTS[_][1]}"\n')
                NUM+=1


        if len(ADVANCED_COPY) > 0:
            midas_file.write("Advanced copy:\n")
            for _ in range(len(ADVANCED_COPY)):
                midas_file.write(f' {NUM}: "{ADVANCED_COPY[_][0]}<::>{ADVANCED_COPY[_][1]}"\n')
                NUM+=1

        if len(VOLUMES) > 0:
            midas_file.write("Volumes:\n")
            for _ in range(len(VOLUMES)):
                midas_file.write(f' {NUM}: "{VOLUMES[_]}"\n')
                NUM+=1

        if len(EXPOSE_PORTS) > 0:
            midas_file.write("Expose ports:\n")
            for _ in range(len(EXPOSE_PORTS)):
                midas_file.write(f' {NUM}: "{EXPOSE_PORTS[_]}"\n')
                NUM+=1

        if len(SETUP_CMDS)> 0 :
            midas_file.write("Setup:\n")
            NUM+=1
            for _ in range(len(SETUP_CMDS)):
                midas_file.write(f' {NUM}: "{SETUP_CMDS[_]}"\n')
                NUM+=1

        if ENTRYPOINT != "":
            midas_file.write("Entry command: ")
            midas_file.write(f'{ENTRYPOINT}\n')

        if len(DEFAULT_CMDS) > 0:
            midas_file.write("Default command: \n")
            for _ in range(len(DEFAULT_CMDS)):
                midas_file.write(f' {NUM}: {DEFAULT_CMDS[_]}\n')
                NUM+=1


def main():
    print("\nINTERACTIVE MODE: BASIL\n")
    print("Docker and Singularity are both containerization technologies that allow you to package up an application and its dependencies into a single image that can be run on any machine. This makes it easy to deploy and manage applications, and to ensure that they are always running in the same environment. Docker is a more popular containerization technology than Singularity. It is easier to use, and there are more Docker images available. However, Singularity is designed for high-performance computing (HPC) environments, and it can be more secure than Docker.")
    print("\nChoose the container type: ")
    print("1. Docker")
    print("2. Singularity")
    container_type = input_("Enter 1 for Docker and 2 for Singularity: ")
    
    if container_type == '1':
        print("\nDOCKER MODE:\n")
        create_basil_file(img_type='docker')
    elif container_type == '2':
        print("\nSINGULARITY MODE:")
        create_basil_file(img_type='singularity')
    else:
        print("Invalid selection, please enter 1 for Docker and 2 for Singularity...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_("Ctrl+C detected.")
        sys.exit(1)

