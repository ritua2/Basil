import os
def create_singularity_def_file():

    print("\nWelcome to Singularity file creation. Follow the prompts below to complete your Singularity Definition File, which will be used to build your Singularity Image.\n")

    # Bootstrap options
    bootstrapOptions = ["docker", "library", "shub", "oras", "scratch"]
    # baseimageOptions = ["ubuntu:23.10", "ubuntu:kinetic", "debian:stable", "node:20.5.0-slim", "postgres:14", "nginx:1.21.6", "nginx:mainline-perl", "python:3.12-rc", "graphcore/tensorflow", "graphcore/pytorch", "php"]

    # Labels
    app_name = input("Enter the name of your application (%label): ")
    app_version = input("Enter the version of your application(%label): ")
    app_author = input("Enter the author's name (%label): ")
    app_description = input("Enter a short description of your application (%label): ")

    # Bootstrap selection
    print("Available set of options for bootstrap method: ")
    for index, option in enumerate(bootstrapOptions, start=1):
        print(f"{index}. {option}")

    bootstrap_selection = input("Select the bootstrap method by entering the corresponding number: ")

    while not bootstrap_selection.isdigit() or not 1 <= int(bootstrap_selection) <= len(bootstrapOptions):
        print("INVALID SELECTION. PLEASE PROVIDE THE INPUT AGAIN.\n")
        bootstrap_selection = input("Select the bootstrap method by entering the corresponding number: ")
    bootstrap = bootstrapOptions[int(bootstrap_selection) - 1]

    base_image = input("Enter the base image for your bootstrap: (for example, ubuntu:23.10): ")

    # Collect package inputs
    packages = []
    while True:
        package = input("Enter a package you want to install or leave empty to finish (%post): ")
        if not package:
            break
        packages.append(package)

    # Collect environment variable inputs
    environments = []
    while True:
        environment = input("Enter an environment variable for your application or leave empty to finish (%environment): ")
        if not environment:
            break
        environments.append(environment)

    helptext = input("Enter the instructions on how to run your program (%help): ")
    app_exec = input("Enter the command to execute your application (%runscript): ")

    # Create the Singularity definition content
    singularity_def = f"""
Bootstrap: {bootstrap}
From: {base_image}

%post
    apt-get -y update
    apt-get -y install {" ".join(packages)}

%labels
    Name {app_name}
    Version {app_version}
    Author {app_author}
    Description {app_description}

%environment
    {os.linesep.join(environments)}

%help
    {helptext}

%runscript
    {app_exec}
"""

    # Write the definition content to a .def file
    def_filename = f"{app_name}_{app_version}.def"
    with open(def_filename, "w") as def_file:
        def_file.write(singularity_def)

    print(f"Singularity definition file '{def_filename}' has been created successfully!")

if __name__ == "__main__":
    create_singularity_def_file()
