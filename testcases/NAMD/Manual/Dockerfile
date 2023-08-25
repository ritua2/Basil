# Use a base image with necessary tools
FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip

# Download NAMD binary
RUN wget https://www-s.ks.uiuc.edu/Research/namd/2.15/download/469773/NAMD_2.15_Linux-x86_64-multicore-CUDA.tar.gz && \
    tar -xzvf NAMD_2.15_Linux-x86_64-multicore-CUDA.tar.gz -C /opt && \
    rm NAMD_2.15_Linux-x86_64-multicore-CUDA.tar.gz

# Set the working directory inside the container
WORKDIR /opt/NAMD_2.15_Linux-x86_64-multicore-CUDA

# Set the default command to run NAMD help
CMD ["./namd2", "--help"]
