# Use a base image with the necessary tools and libraries
FROM ubuntu:latest

# Install required packages
RUN apt-get update 

RUN apt-get install -y wget ncbi-blast+

# Set the working directory inside the container
WORKDIR /

# Define the entrypoint command to run BLAST with the help flag
ENTRYPOINT ["blastp", "-help"]
