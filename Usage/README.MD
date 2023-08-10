Building and Running a Docker Image after generating a Dockerfile through Basil

This guide will walk you through the process of building a Docker image using the provided Dockerfile and then running a container from that image on Windows, Linux, and macOS systems.

Prerequisites

Before we get started, ensure that you have Docker installed on your system. If you do not, then follow the steps below:

For Windows:
1. Go to the Docker website: https://www.docker.com/get-started
2. Download the Docker Desktop Installer.exe file
3. Run the .exe file to run and finish the installation by following the on-screen instructions

For macOS:
1. Open a terminal window
2. Run the following command to download the installer for Docker: curl -fsSL https://get.docker.com -o get-docker.sh
3. Now run this command to install Docker: sudo sh get-docker.sh

For Linux:
1. Open a terminal window
2. Run the following command: sudo apt-add-repository https://download.docker.com/linux/ubuntu/repo/deb
3. Next, run this command: sudo apt update
4. Now, run this command: sudo apt install docker-ce
5. Finally, run this command to check if Docker has been installed correctly: docker version 

CASE 1: Pushed the image to Docker Hub account by providing 'Username' and 'Access Token'

Step 1: Login to your Docker Hub account and locate the image that was pushed after generating the Dockerfile through Basil, and click on it.
Step 2: Click on 'Public View' and go to the 'Tags' banner button. You should see a 'docker pull [image name]' command there, copy the whole command.
Step 3: Paste the command in a terminal session and hit enter, it should pull the image from your Docker Hub account to your system.
Step 4: Run the 'docker image ls' command and copy the image ID of the image you just pulled.
Step 5: Finally, run this command, 'docker run [image ID here]' and it should run your image and perform the task it was programmed to do.

CASE 2: Pushed the image to Docker Hub account but did NOT provide 'Username' and 'Access Token'

Step 1:  Go to https://hub.docker.com/ and type 'basilproject' in the search bar located in the top left part of the website. You do not need to have a Docker Hub account to perform this action.
Step 2: Locate the image that was pushed here, the image name should have your username in it to make it easier to identify.
Step 3: Copy the 'Docker Pull Command' provided on the webpage and paste it into your terminal session and hit enter.
Step 4: Once the pull has completed, run the 'docker image ls' command and copy the image ID for your pulled image
Step 5: Finally, run 'docker run [image ID]' command and it should run your image.

CASE 3: Did not push the image to Docker Hub

Step 1: Check your email, you should have an email from 'icomputeus@gmail.com'. It should have a link to download the file as well as instructions on how to run it, they are also provided here.
Step2: Click the link to download the file, once the file has downloaded, open terminal and navigate to the folder where the .tar.gz file is located.
Step 3: Run this command, docker load < [image name.tar.gz] and wait for the image to be loaded.
Step 4: Confirm the image is available on your system by running 'docker image ls'. Copy the Image ID provided here.
Step 5: Run this command, 'docker run [image ID]', and you're done!

More features are coming soon so please keep an eye out for updates, and we look forward to your continued patronage.

Thank you
Team BASIL
