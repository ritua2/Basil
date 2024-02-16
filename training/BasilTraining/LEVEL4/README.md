# Level 4 - Containerize Jetscape Application

In this level, you will containerize Jetscape application into docker and singularity images either by using iSpec form or basil standalone version.

# Contents
* This directory is structured as follows:
```bash
.
├── README.md
└── setup.sh
```
* README.md: This file explains the concepts and a hands-on exercise to practice the concepts.
* setup.sh: This script installs all the necessary software and dependencies to run the Jetscape application. You can use this input to the iSpec form to containerize the application.


# Steps
### Containerize the application
#### Containerize the application using iSpec form
* Go to [icompute.us](https://icompute.us) and click on "Sign in".
* You can sign in using CILogon option or create a new account and sign in.
* Once you are signed in, click on "iSpec" tab to open the iSpec form.
* You don't need to upload any project directory to iSpec. 
* Select the meta tags.
    * Select "training" in the meta tags.
* Select the image type.
    * Select Ubuntu:20.04 as the base image because the setup script is tested with Ubuntu:20.04.
* Setup/Installation Commands
    * Copy the contents of setup.sh script to "Setup/Installation Commands" section.
* Click on "Submit" button to submit the containerization job.
* You will receive an email once the job is completed.
* Once the job is completed, you can download the docker/singularity image from the email you received from iCompute.
* To run the image locally follow the instructions in the email.

#### Containerize the application using Basil's standalone version
* Go to LEVEL4 directory    
```bash
cd LEVEL4
```
* Start the basil standalone version
```bash
docker run --platform linux/amd64 --rm -it -v .:/project basilproject/basil_sanjeethboddigm_1708035159:latest
```
* Once you start the basil standalone version, you will be prompted for the information similar to the iSpec form.
* Provide the necessary information to containerize the application into docker and singularity images.
    * Use ubuntu:focal as the base image.
    * Use the following setup commands from the setup.sh script
* Once done, basil standalone version will generate the docker/singularity definition files.
* To build dockerfile & run the docker image, run the following command:
```bash
docker build -t jetscape:latest .
docker run -it jetscape:latest
```
* To build singularity definition file & run the singularity image, run the following command:
```bash
singularity build --fakeroot jetscape.sif singularity.def
./jetscape.sif
```

