# Level 1 - Todo App

In this level, you will learn the basics of Basil and use it to containerize a simple web-application (a ToDo-list app) with Docker and Singularity.

# Contents
* This directory is structured as follows:
```bash
.
├── README.md
├── requirements.txt
├── solution
│   └── setup.sh
└── src
    ├── templates
    │   └── home.html
    └── webapp.py
```
* README.md: This file explains the concepts and a hands-on exercise to practice the concepts.
* solution: This directory contains setup.sh script to solve this particular level
* src: This directory contains the source code of the level. 
    * It contains a Python script named webapp.py that starts a web server on port 5000 and a directory named templates that contains a html file named home.html.


# Steps
### Create a setup script
The goal of this step is to create setup script that will install all the necessary software and dependencies to run the application.
* Create a setup script that will install all the necessary software and dependencies to run the python script with out any human intervention.
    * All the python dependencies are listed in the requirements.txt file. You can use the pip command to install the dependencies.
* Once done, you can test by running the script to install the software and dependencies and run the application. If you are unable to complete this step, you can use the setup.sh script provided in the solution directory.

### Containerize the application using Basil's iSpec form
The goal of this step is to containerize the application using Basil's iSpec form.
* Go to [icompute.us](https://icompute.us) and click on "Sign in".
* You can sign in using CILogon option or create a new account and sign in.
* Once you are signed in, click on "iSpec" tab to open the iSpec form.

* Upload your project directory to iSpec.
    * Upload the LEVEL1 folder to iSpec.
    * Please click upload button below the "Choose Files" input box.
* Provide the directory where Basil stores the generated files
    * Since you have uploaded the LEVEL1 folder, it is automatically selected as the project directory.
* Select the meta tags.
    * Select "training" in the meta tags.
* Select the image type.
    * We will repeat the containerization process twice to containerize the application into both docker and singularity images. So, you can select either "Docker" or "Singulariy" as the image type.
* Select the base image.
    * Select the base image as ubuntu if you are working on ubuntu/debian platform. Else, select the appropriate base image.
* Working Directory
    * Let's keep the working directory as it is. We will discuss about it in the next levels.
* Environment Variables
    * The application does not require any environment variables. So, you can skip this section.
* Copy files from project directory to image
    * to copy the script to the image, type the following in the "Copy files from project directory to image" section:
    ```bash
    src/webapp.py:/webapp.py
    src/templates:/templates
    requirements.txt:/requirements.txt
    ``` 
    * This will copy the webapp.py script and requirements.txt file from the project directory to the root directory of the image.
* Advanced copy
    * You can skip this section.
* Expose ports
    * The application requires port 5000 to be exposed. So, type the following in the "Expose ports" section:
    ```bash
    5000/tcp
    ```
* Volumes
    * The application does not require any volumes to be mounted. So, you can skip this section.
* Setup/Installation Commands
    * Copy the contents of setup.sh script to "Setup/Installation Commands" section.
* Entry Command
    * Type the following in the "Entry Command" section:
    ```bash
    python3 /webapp.py
    ```
    * This command will run the webapp.py script in the image and start the web server.
* Execution Command
    * You can skip this section.
* Click on "Submit" button to submit the containerization job.
* You will receive an email once the job is completed.
* Once the job is completed, you can download the docker and singularity images from the email you received from iCompute.

### Run the containerized application
The goal of this step is to run the containerized application and verify that it works as expected.
* You might have received an email with the link to download the image.
* Follow the instructions in the email to run the image.
