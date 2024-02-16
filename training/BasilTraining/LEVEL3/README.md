# Level 3 - Flying Donut

In this level, you will learn the basics of Basil and use it to containerize a simple application which outputs flying donut into docker and singularity images.

# Contents
* This directory is structured as follows:
```bash
.
├── README.md
├── solution
│   └── setup.sh
└── src
    └── donut.c
```
* README.md: This file explains the concepts and a hands-on exercise to practice the concepts.
* solution: This directory contains setup.sh script to solve this particular level
* src: This directory contains the source code of the level. Specifically, it contains a C program named donut.c which outputs a flying donut.


We will use the basil standalone version to containerize the application. The standalone version of basil is a command line tool that can be used to containerize an application without using the iSpec form. The standalone version of basil is useful when you want to containerize an application without using the iSpec form. 

# Steps
* Go to LEVEL3 directory    
```bash
cd LEVEL3
```
* Start the basil standalone version
```bash
docker run --platform linux/amd64 --rm -it -v .:/project basilproject/basil_sanjeethboddigm_1708035159:latest
```
* Once you start the basil standalone version, you will be prompted for the information similar to the iSpec form. 
* Provide the necessary information to containerize the application into docker and singularity images.
* Once done, basil standalone version will generate the docker/singularity definition files.
* To build dockerfile & run the docker image, run the following command:
```bash
docker build -t donut:latest .
docker run -it donut:latest
```
* To build singularity definition file & run the singularity image, run the following command:
```bash
singularity build --fakeroot donut.sif singularity.def
./donut.sif
```
