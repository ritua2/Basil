# Docker-Exercise - PART 2 Docker Image with Jupyter, Pycharm IDE + Anaconda

The Dockerfile contains the necessary instructions for downloading the latest Pycharm version and to show 2 URL's that point to a Jupyter Notebook. In my testing, the first link was always invalid and the second link always worked. But I was unable to get Pycharm to open for some reason, and tried troubleshooting with different versions and multiple commands but the errors ranged from invalid commands to incorrect file path.

Running the container is as simple as navigating to the folder and typing these cmd in the terminal:
docker build -t myJPAimage .
docker run -p 8888:8888 -it myJPAimage

For running Pycharm we open a new terminal and type in:
docker exec -it <container_name> /bin/bash and then typing pycharm.sh to launch Pycharm

This was the cmd I found through some online digging but it always shows errors.
