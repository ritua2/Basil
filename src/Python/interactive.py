#to be tested
#!/usr/bin/python
import os
import re

def input_(prompt):
    return input("\n" + prompt + " ")

def main():
    print("\nINTERACTIVE MODE: MIDAS\n")
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
    ]

    print("Available set of base images for MIDAS: ")
    for index, image_and_pkg_manager in enumerate(images_and_package_manager, start=1):
        print(f"{index}. {image_and_pkg_manager[0]}")

    selection = input_(">>> Please select the base image by entering its number: ")

    while not selection.isdigit() or not 1 <= int(selection) <= len(images_and_package_manager):
        print("INVALID SELECTION. PLEASE PROVIDE THE INPUT AGAIN.\n")
        selection = input_(">>> Please select the base image by entering its number: ")
    BASE_IMAGE, PKG_MANAGER = images_and_package_manager[int(selection) - 1]

    WORKDIR = input_(">>> Enter work directory: [OPTIONAL]")

    ENV_VARIABLES = []
    print(">>> Enter the environment variables. Press ENTER to skip when you don't have anything more to enter ...")
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
    print(">>> Enter the contents that you want to package with the docker file. Press ENTER to skip when you don't have anything more to enter ...")
    while True:
        CONTENT_SRC = input_(f"[{len(CONTENTS)+1}]: INPUT SOURCE FILE PATH: ")
        if(CONTENT_SRC==""):
            print()
            break

        CONTENT_DEST = input_(f"[{len(CONTENTS)+1}]: INPUT DESTINATION FILE PATH INSIDE IMAGE: ")

        confirmation = input_(f"Do you want to add '{CONTENT_SRC}' to '{CONTENT_DEST}'? [Y/n]\n")
        if confirmation.lower() != 'n':
            CONTENTS.append((CONTENT_SRC, CONTENT_DEST))

    ADVANCED_COPY = []
    print(">>> ADVANCED COPY: Enter the contents that you want to package with the docker file. Press ENTER to skip when you don't have anything more to enter ...")
    note = """
        Advanced way to copy files to Docker image
        - Web File Downloads: Download files directly from the web and add them to your Docker images.
        - Flexible Copy Operations: Copy files and folders based on specific patterns to defined locations within your Docker images.
        - Simple Decompression: Easily decompress tar files without any manual effort.
        Examples:
            1. Web File Download:
                https://example.com/sample-file.txt:/path/to/destination/sample-file.txt
            2. Copy Files using Regex Matches:
                myapp-*.js:/app/
            3. Simplified Decompression of Tar Files:
                myapp.tar.gz:/destination/folder/
    """
    print(note)
    while True:
        CONTENT_SRC = input_(f"[{len(ADVANCED_COPY)+1}]: INPUT SOURCE FILE: ")
        if(CONTENT_SRC==""):
            print()
            break

        CONTENT_DEST = input_(f"[{len(CONTENTS)+1}]: INPUT DESTINATION FILE PATH INSIDE IMAGE: ")

        confirmation = input_(f"Do you want to add '{CONTENT_SRC}' to '{CONTENT_DEST}'? [Y/n]\n")
        if confirmation.lower() != 'n':
            ADVANCED_COPY.append((CONTENT_SRC, CONTENT_DEST))

    VOLUMES = []
    print(">>> Enter the volumes that you want to mount with the docker image. Press ENTER to skip when you don't have anything more to enter ...")
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
    print(">>> Enter the ports that you want to expose. Press ENTER to skip when you don't have anything more to enter ...")
    note = """
        Expose ports will expose the ports to the host machine. For example if you provide "8080", the port 8080 will be exposed to the host machine and you can access the application running inside the docker container from your host machine.
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

    PACKAGES = []
    print(">>> Enter the packages that you want to install. Press ENTER to skip when you don't have anything more to enter ...")
    while True:
        PKG = input_(f"[{len(PACKAGES)+1}]: ")
        if(PKG==""):
            print()
            break
        confirmation = input_(f"Do you want to install '{PKG}'? [Y/n]\n")
        if confirmation.lower() != 'n':
            PACKAGES.append(PKG)

    SETUP_CMDS = []
    print(">>> Enter the commands to configure the project environment. Press ENTER to skip when you don't have anything more to enter ...")

    while True:
        CMD = input_(f"[{len(SETUP_CMDS)+1}]: ")
        if (CMD == ""):
            print()
            break
        confirmation = input_(f"Do you want to add command `${CMD}` to setup your project environment? [Y/n]\n")
        if confirmation.lower() != 'n':
            SETUP_CMDS.append(CMD)

    ENTRYPOINT = input_("Enter the entry command. "
                        "Entry command runs every time you run the image. "
                        "By default, Entry command starts a new shell session: [OPTIONAL]")

    DEFAULT = input_("Enter the default command:")

    # license work
    def load_license_files(license_directory):
        licenses = []
        for filename in os.listdir(license_directory):
            if filename.endswith(".txt"):
                with open(os.path.join(license_directory, filename), 'rb') as file:
                    licenses.append((filename[:-4], file.read().decode('utf-8'), os.path.join(license_directory, filename)))
        return licenses

    # license_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../licenses")
    script_directory = os.path.dirname(os.path.abspath(__file__))
    license_directory = os.path.join(script_directory, "../licenses")
    license_list = load_license_files(license_directory)

    def license_yes_no(prompt):
        response = input(prompt + " [y/n] ").strip().lower()
        return response == 'y' or response == 'yes'

    include_license = license_yes_no("Would you like to include a license?")

    if include_license:
        print("Available licenses: ")
        for index, (license_name, _, _) in enumerate(license_list, start=1):
            print(f"{index}. {license_name}")

        selection = input_(">>> Please select a license by entering its number: ")

        while not selection.isdigit() or not 1 <= int(selection) <= len(license_list):
            print("INVALID selection. Please provide the input again...\n")
            selection = input_(">>> Please select a license by entering its number: ")

        selected_license_name, selected_license_text, _ = license_list[int(selection) - 1]

        selected_license_path = os.path.join(license_directory, f"{selected_license_name}.txt")
        user_license_path = os.path.expanduser("~/LICENSE.txt")
        with open(selected_license_path, 'rb') as source_file, open(user_license_path, 'wb') as dest_file:
            dest_file.write(source_file.read())

        CONTENTS.append(("LICENSE.txt", "LICENSE"))

    # end license work

    with open('midas.yml','w+') as midas_file:
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
                midas_file.write(f'  {ENV_VARIABLES[_][0]}: {ENV_VARIABLES[_][1]}\n')
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

        if len(PACKAGES) + len(SETUP_CMDS)> 0 :
            midas_file.write("Setup:\n")
            if PKG_MANAGER == "apt":
                midas_file.write(f' {NUM}: "apt-get update"\n')
            elif PKG_MANAGER == "yum":
                midas_file.write(f' {NUM}: "yum update"\n')
            elif PKG_MANAGER == "apk":
                midas_file.write(f' {NUM}: "apk update"\n')
            NUM+=1

            for _ in range(len(PACKAGES)):
                if PKG_MANAGER == "apt":
                    midas_file.write(f' {NUM}: "{PKG_MANAGER} install -y {PACKAGES[_]}"\n')
                elif PKG_MANAGER == "yum":
                    midas_file.write(f' {NUM}: "{PKG_MANAGER} install -y {PACKAGES[_]}"\n')
                elif PKG_MANAGER == "apk":
                    midas_file.write(f' {NUM}: "{PKG_MANAGER} add {PACKAGES[_]}"\n')
                NUM+=1

            for _ in range(len(SETUP_CMDS)):
                midas_file.write(f' {NUM}: "{SETUP_CMDS[_]}"\n')
                NUM+=1

        if ENTRYPOINT != "":
            midas_file.write("Entry command: ")
            midas_file.write(f'{ENTRYPOINT}\n')

        if DEFAULT != "":
            midas_file.write("Default command: ")
            midas_file.write(f'{DEFAULT}\n')

if __name__ == "__main__":
    main()
