# Use a base image with necessary tools
FROM ubuntu:23.10

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

# Copy the water_simulation.namd input file
COPY water_simulation.namd /opt/NAMD_2.15_Linux-x86_64-multicore-CUDA/

# Set the default command to run NAMD with the input file
CMD ["./namd2", "water_simulation.namd"]
