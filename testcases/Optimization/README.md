# Docker-Exercise PART 1 - Optimize a Docker Image

Use a smaller base image: The current base image used is python:3.5-slim which is relatively small, but there are even smaller base images available. Using a smaller base image can improve build and deployment times.

Combine some of the RUN commands: Some of the RUN commands can be combined into a single RUN command to reduce the number of layers in the final image. This can help reduce the overall size of the image.

Use COPY instead of curl: Instead of using curl to download files, you can include the files in the build context and use the COPY command to copy them into the container. This can help reduce the number of network requests made during the build process.

In this end, I used a newer version of the python base image (3.12), combined some of the RUN commands, and used COPY to copy files into the container. I also added a couple of improvements to the way the MGLTools are installed and sourced, these were sourced from Stack-Overflow, Git-Hub and FreeCodeCamp articles.

