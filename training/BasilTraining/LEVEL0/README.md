# Level 0 - Hello Basil

In this level, you will learn the basics of using the Basil web-portal and use it to containerize a "Hello Basil" application with Docker or Singularity.

# Contents
* This directory is structured as follows:
```bash
.
├── README.md
├── solution
│   └── setup.sh
└── src
    └── hellobasil.py
```
* README.md: This file explains the concepts and a hands-on exercise to practice the concepts.
* solution: This directory contains setup.sh script to solve this particular level.
* src: This directory contains the source code used for this exercise. Specifically, it contains a Python script named hellobasil.py that prints "Hello Basil".



# Steps
### Create a setup script
The goal of this step is to create a setup script that will install all the necessary software and dependencies to run the "Hello Basil" application.
* Create a setup script that will install all the necessary software and dependencies to run the python script without any human intervention. 
* Once done, you can test by running the script to install the software and dependencies, and run the application. If you are unable to complete this step, you can use the setup.sh script provided in the solution directory.

### Containerize the application using Basil's iSpec form
The goal of this step is to containerize the application using Basil's iSpec form.
* Go to [icompute.us](https://icompute.us) and click on "Sign in".
* You can sign in using CILogon option or create a new account and sign in.
* Once you are signed in, click on "iSpec" tab to open the iSpec form.

* Upload your project directory to iSpec.
    * Upload the LEVEL0 folder to iSpec. 
    * Please click upload button below the "Choose Files" input box.
* Provide the directory where Basil stores the generated files
    * Since you have uploaded the LEVEL0 folder, it is automatically selected as the project directory.
* Select the meta tags.
    * Select "training" in the meta tags.
* Select the image type.
    * We will repeat the containerization process twice to generate both Docker and Singularity images. Therefore, you can select either "Docker" or "Singulariy" as the image type.
* Select the base image.
    * Select the base image as Ubuntu if you are working on Ubuntu/Debian platform. Else, select the appropriate base image.
* Working Directory
    * Let's keep the working directory as it is. We will discuss about it in the next levels.
* Environment Variables
    * The application does not require any environment variables. So, you can skip this section.
* Copy files from project directory to image
    * to copy the script to the image, type the following in the "Copy files from project directory to image" section:
    ```bash
    src/hellobasil.py:/hellobasil.py
    ``` 
    * This will copy the hellobasil.py script from the project directory to the root directory of the image.
* Advanced copy
    * You can skip this section.
* Expose ports
    * The application does not require any ports to be exposed. So, you can skip this section.
* Volumes
    * The application does not require any volumes to be mounted. So, you can skip this section.
* Setup/Installation Commands
    * Copy the contents of setup.sh script to "Setup/Installation Commands" section.
* Entry Command
    * Type the following in the "Entry Command" section:
    ```bash
    python3 /hellobasil.py
    ```
    * This command will run the hellobasil.py script in the image.
* Execution Command
    * You can skip this section.
* Click on "Submit" button to submit the containerization job.
* You will receive an email once the job is completed.
* Once the job is completed, you can download the Docker or Singularity images from the email you received from iCompute.

### Run the containerized application
The goal of this step is to run the containerized application and verify that it works as expected.
* You might have received an email with the link to download the image.
* Follow the instructions in the email to run the image.
