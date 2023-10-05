def create_singularity_def_file():

    print("\nWelcome to Singularity file creation. Follow the prompts below to complete your Singularity Definition File, which will be used to build your SIngularity Image.\n")

    # bootstrap options
    bootstrapOptions = ["docker", "library", "shub", "oras", "scratch"]
    baseimageOptions = ["ubuntu:23.10", "ubuntu:kinetic", "debian:stable", "node:20.5.0-slim", "postgres:14", "nginx:1.21.6", "nginx:mainline-perl", "python:3.12-rc", "graphcore/tensorflow", "graphcore/pytorch", "php"]

    # labels
    app_name = input("Enter the name of your application: ")
    app_version = input("Enter the version of your application: ")
    app_author = input("Enter the author's name: ")
    app_description = input("Enter a short description of your application: ")

    # show bootstrap preffered options
    print("Available set of options for bootstrap method: ")
    for index, option in enumerate(bootstrapOptions, start=1):
        print(f"{index}. {option}")

    selection = input("Select the bootstrap method by entering the corresponding number: ")

    while not selection.isdigit() or not 1 <= int(selection) <= len(bootstrapOptions):
        print("INVALID SELECTION. PLEASE PROVIDE THE INPUT AGAIN.\n")
        selection = input("Select the bootstrap method by entering the corresponding number: ")
    bootstrap = bootstrapOptions[int(selection) - 1]

    base_image = input("Enter the base image for your bootstrap: (for eg. ubuntu:23.10): ")    
    package = input("Enter the package(s) you want to install: ")
    environment1 = input("Enter the environment variables for your application: ")
    environment2 = input("Enter the environment variables for your application: ")
    helptext = input("Enter the instructions on how to run your program: ")
    app_exec = input("Enter the command to execute your application: ")

    # Create the Singularity definition content
    singularity_def = f"""\
Bootstrap: {bootstrap}
From: {base_image}

%post
    apt-get -y update
    apt-get -y install {package}

%labels
    Name {app_name}
    Version {app_version}
    Author {app_author}
    Description {app_description}

%environment
    {environment1}
    {environment2}

%help
    {helptext}

%runscript
    {app_exec}
"""

    # Write the definition content to a .def file
    def_filename = f"{app_name}_{app_version}.def"
    with open(def_filename, "w") as def_file:
        def_file.write(singularity_def)

    print(f"Singularity definition file '{def_filename}' created successfully!")

if __name__ == "__main__":
    create_singularity_def_file()
