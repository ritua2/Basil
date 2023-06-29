#!/usr/bin/python
print("INTERACTIVE MODE: MIDAS")

WORKDIR = input(">>> Enter work directory: [OPTIONAL]")

ENV_VARIABLES = []
print(">>> Enter the environment variables. Press ENTER to skip...")
while True:
    ENV_VAR = input(f"[{len(ENV_VARIABLES)+1}]: VARIABLE NAME: ")
    if (ENV_VAR == ""):
        break
    ENV_VAR_VAL = input(f"[{len(ENV_VARIABLES)+1}]: VARIABLE VALUE: ")

    confirmation = input(f"Do you want to add `{ENV_VAR}={ENV_VAR_VAL}`? [Y/n]]\n")
    if confirmation.lower() != 'n':
        ENV_VARIABLES.append((ENV_VAR,ENV_VAR_VAL))

CONTENTS = []
print(">>> Enter the contents that you want to package with the docker file. Press ENTER to skip...")
while True:
    CONTENT_SRC = input(f"[{len(CONTENTS)+1}]: INPUT SOURCE FILE PATH: ")
    if(CONTENT_SRC==""):
        break
    
    CONTENT_DEST = input(f"[{len(CONTENTS)+1}]: INPUT DESTINATION FILE PATH INSIDE IMAGE: ")

    confirmation = input(f"Do you want to add '{CONTENT_SRC}' to '{CONTENT_DEST}'? [Y/n]\n")
    if confirmation.lower() != 'n':
        CONTENTS.append((CONTENT_SRC, CONTENT_DEST))

PACKAGES = []
print(">>> Enter the packages that you want to install. Press ENTER to skip...")
while True:
    PKG = input(f"[{len(PACKAGES)+1}]: ")
    if(PKG==""):
        break
    confirmation = input(f"Do you want to install '{PKG}'? [Y/n]\n")
    if confirmation.lower() != 'n':
        PACKAGES.append(PKG)


SETUP_FILE = input(">> Enter setup file: [OPTIONAL]")

SETUP_CMDS = []
print(">>> Enter the setup commands. Press ENTER to skip...")

while True:
    CMD = input(f"[{len(SETUP_CMDS)+1}]: ")
    if (CMD == ""):
        break
    confirmation = input(f"Do you want to add command `${CMD}` to the setup process? [Y/n]\n")
    if confirmation.lower() != 'n':
        SETUP_CMDS.append(CMD)


ENTRYPOINT = input("Enter the entry command. Entry command runs every time you run the image. By default, Entry command starts a new shell session: [OPTIONAL]")

DEFAULT = input("Enter the default command:")

with open('midas.yml','w') as midas_file:
    # ADDING BASE IMAGE SO THAT THE YAML FILE IS VALID
    midas_file.write("Base: \"ubuntu:latest\"\n")

    NUM = 1

    midas_file.write("Working directory:\n")
    midas_file.write(f' 1: "{WORKDIR}"\n')
    NUM+=1

    midas_file.write("Environmental variables:\n")
    for _ in range(len(ENV_VARIABLES)):
        midas_file.write(f' {NUM}:\n')
        midas_file.write(f'  {ENV_VARIABLES[_][0]}: {ENV_VARIABLES[_][1]}\n')
        NUM += 1

    midas_file.write("Contents:\n")
    for _ in range(len(CONTENTS)):
        midas_file.write(f' {NUM}: "{CONTENTS[_][0]}:{CONTENTS[_][1]}"\n')
        NUM+=1

    midas_file.write("Setup:\n")
    for _ in range(len(PACKAGES)):
        midas_file.write(f' {NUM}: "apt-get install {PACKAGES[_]}"\n')
        NUM+=1
    for _ in range(len(SETUP_CMDS)):
        midas_file.write(f' {NUM}: "{SETUP_CMDS[_]}"\n')
        NUM+=1
    
    midas_file.write("Entry command: ")
    midas_file.write(f'{ENTRYPOINT}\n')

    midas_file.write("Default command: ")
    midas_file.write(f'{DEFAULT}\n')






