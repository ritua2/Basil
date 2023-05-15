# Docker-Exercise
Programming Exercises

PART 1 Optimize a Docker Image

Use a smaller base image: The current base image used is python:3.5-slim which is relatively small, but there are even smaller base images available. Using a smaller base image can improve build and deployment times.
Combine some of the RUN commands: Some of the RUN commands can be combined into a single RUN command to reduce the number of layers in the final image. This can help reduce the overall size of the image.
Use COPY instead of curl: Instead of using curl to download files, you can include the files in the build context and use the COPY command to copy them into the container. This can help reduce the number of network requests made during the build process.

In this end, I used a newer version of the python base image (3.12), combined some of the RUN commands, and used COPY to copy files into the container. I also added a couple of improvements to the way the MGLTools are installed and sourced, these were sourced from Stack-Overflow, Git-Hub and FreeCodeCamp articles.

PART 2 Docker Image with Jupyter, Pycharm IDE + Anaconda

The Dockerfile contains the necessary instructions for downloading the latest Pycharm version and to show 2 URL's that point to a Jupyter Notebook. In my testing, the first link was always invalid and the second link always worked. But I was unable to get Pycharm to open for some reason, and tried troubleshooting with different versions and multiple commands but the errors ranged from invalid commands to incorrect file path.

Running the container is as simple as navigating to the folder and typing these cmd in the terminal:
docker build -t myJPAimage .
docker run -p 8888:8888 -it myJPAimage

For running Pycharm we open a new terminal and type in:
docker exec -it <container_name> /bin/bash and then typing pycharm.sh to launch Pycharm

This was the cmd I found through some online digging but it always shows errors.
