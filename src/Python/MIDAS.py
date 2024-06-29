#!/usr/bin/env python

"""
Main MIDAS standalone program
"""

import argparse
import getpass
import os
import re
import sys
import subprocess
import fileinput
import color_print
import parser as MIDAS_parser

def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'y', "Y", '1'):
        return True
    elif v.lower() in ('no', 'n', "N", '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')



# Argument parsing
parser = argparse.ArgumentParser()

base_images = ["ubuntu:23.10", "ubuntu:kinetic",
               "debian:stable", "debian:11",
               "node:lts", "node:19-bullseye",
               "postgres:13.11", "postgres:14",
               "nginx:1.21.6", "nginx:mainline",
               "python:3.12-rc", "python:3.10.4",
               "graphcore/tensorflow", "graphcore/pytorch"]

parser.add_argument("--ignore-warnings", type=str2bool, nargs='?', const=True, default=False, help="Ignore all warnings, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("--ignore-cmd-warnings", type=str2bool, nargs='?', const=True, default=False, help="Ignore CMD warnings, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("--ignore-copy-warnings", type=str2bool, nargs='?', const=True, default=False, help="Ignore COPY warnings, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("--ignore-run-warnings", type=str2bool, nargs='?', const=True, default=False, help="Ignore RUN warnings, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("--strict", type=str2bool, nargs='?', const=True, default=False, help="Treat warnings as errors, stop program when one occurs, 'yes'/'y'/'Y'/'1' for True")

parser.add_argument("-f", "--file", type=str, nargs='?', const=True, default="midas.yml", help="Input file")
parser.add_argument("-o", "--output", type=str, nargs='?', const=True, help="Output image path")

parser.add_argument("-t", "--tag", type=str, nargs='?', const=True, default=False, help="Name:version of the image if built, by default, no image will be built")
parser.add_argument("--timeout", type=int, nargs='?', const=True, default=60, help="Max time in s (int) for building docker image, set to 60 s by default")

parser.add_argument("--push", type=str2bool, nargs='?', const=True, default=False, help="Pushes to dockerhub, 'yes'/'y'/'Y'/'1' for True")
parser.add_argument("-u", "--username", type=str, nargs='?', const=True, default=False, help="Dockerhub username, will prompt the user if not set and pushing")

parser.add_argument("-b", "--base-image", type=str, choices=base_images, help="Base image to be used")

args = parser.parse_args()

if not os.path.exists(args.file):
    sys.exit("ERROR: File " + args.file + " does not exist.")

provided_data = MIDAS_parser.parse_commands(args.file)

if MIDAS_parser.base_check(provided_data)[1]:
    sys.exit("Necessary argument 'Base' is missing from input file")


def create_image_definition_file():
    docker_instructions = MIDAS_parser.order_inputs(provided_data)

    if docker_instructions[1]:
        sys.exit(docker_instructions[0])

    docker_instructions = docker_instructions[0]

    #process warnings
    warnings_to_check = {"CMD": not args.ignore_cmd_warnings,
                    "COPY": not args.ignore_copy_warnings,
                    "RUN": not args.ignore_run_warnings
                    }

    docker_translator = {
        "Contents":"COPY",
        "Setup":"RUN",
        "Entry command":"ENTRYPOINT",
        "Default command":"CMD",
        "Volumes": "VOLUME",
        "Expose ports": "EXPOSE",
        "Advanced copy": "ADD",
        "Setup2": "RUN",
        "Copy From Base": "COPY"
    }

    midas_translator = {v: k for k, v in docker_translator.items()}
    instruction_types = []

    if not args.ignore_warnings:
        for instruction in docker_instructions:
            instruction_types.append(instruction[2])
        else:
            if "Default command" in provided_data:
                instruction_types.append("Default command")

        provided_docker_instruction_types = [ docker_translator[b] for b in list(set(instruction_types)) if b in docker_translator]
        types_to_check = [inst for inst in warnings_to_check if warnings_to_check[inst]==True]

        for checking_type in types_to_check:

            if checking_type not in provided_docker_instruction_types:
                color_print.color_print("Warning: No '"+midas_translator[checking_type]+"' provided, this corresponds to a docker '"+checking_type+"' instruction", "YELLOW")
                if args.strict:
                    color_print.color_print("Error: No '"+midas_translator[checking_type]+"' provided, strict parsing", "RED")
                    sys.exit()

    # Create dockerfile/specification file
    image_file = MIDAS_parser.create_imagefile(args.file, args.output)
    os.system('cat '+image_file)


    if not args.tag:
        sys.exit()

    

create_image_definition_file()

