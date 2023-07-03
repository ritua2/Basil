#!/usr/bin/python
def input_(prompt):
    return input("\n"+prompt+" ")

def main():
    print("INTERACTIVE MODE: MIDAS\n")
    images_and_package_manager = [
        ("ubuntu:23.10", "apt"),
        ("ubuntu:kinetic", "apt"),
        ("debian:stable", "apt"),
        ("debian:11", "apt"),
        ("node:lts","apt"),
        ("node:19-bullseye", "apt"),
        ("postgres:13.11", "apt"),
        ("postgres:14", "apt"),
        ("nginx:1.21.6", "apt"),
        ("nginx:mainline", "apt"),
        ("python:3.12-rc", "apt"),
        ("python:3.10.4", "apt"),
        ("graphcore/tensorflow", "apt"),
        ("graphcore/pytorch", "apt"),
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

    with open('midas.yml','w') as midas_file:
        # ADDING BASE IMAGE SO THAT THE YAML FILE IS VALID
        midas_file.write(f"Base: \"{BASE_IMAGE}\"\n")

        NUM = 1
        if WORKDIR != "":
            midas_file.write("Working directory:\n")
            midas_file.write(f' 1: "{WORKDIR}"\n')
            NUM+=1

        if len(ENV_VARIABLES) > 0:
            midas_file.write("Environmental variables:\n")
            for _ in range(len(ENV_VARIABLES)):
                midas_file.write(f' {NUM}:\n')
                midas_file.write(f'  {ENV_VARIABLES[_][0]}: {ENV_VARIABLES[_][1]}\n')
                NUM += 1

        if len(CONTENTS) > 0:
            midas_file.write("Contents:\n")
            for _ in range(len(CONTENTS)):
                midas_file.write(f' {NUM}: "{CONTENTS[_][0]}:{CONTENTS[_][1]}"\n')
                NUM+=1

        if len(PACKAGES) + len(SETUP_CMDS)> 0 :
            midas_file.write("Setup:\n")
            if PKG_MANAGER == "apt":
                midas_file.write(f' {NUM}: "apt-get update"\n')
            elif PKG_MANAGER == "yum":
                midas_file.write(f' {NUM}: "yum update"\n')
            NUM+=1

            for _ in range(len(PACKAGES)):
                if PKG_MANAGER == "apt":
                    midas_file.write(f' {NUM}: "{PKG_MANAGER} install -y {PACKAGES[_]}"\n')
                elif PKG_MANAGER == "yum":
                    midas_file.write(f' {NUM}: "{PKG_MANAGER} install -y {PACKAGES[_]}"\n')
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