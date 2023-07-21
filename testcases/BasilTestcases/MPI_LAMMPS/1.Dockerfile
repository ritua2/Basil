# Use the official Ubuntu image with SSL certificates and necessary packages
FROM ubuntu:latest

# Install prerequisites
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    ca-certificates \
    apt-transport-https \
    gnupg \
    && apt-get clean

# Clone the LAMMPS repository
RUN git config --global http.sslVerify false
RUN git clone -b release https://github.com/lammps/lammps.git /mylammps

# Set the working directory to the LAMMPS directory
WORKDIR /mylammps

# Create and switch to the build directory
RUN mkdir build
RUN cd build

# Configure LAMMPS using CMake
RUN cmake ..

# Build LAMMPS
RUN cmake --build .

# Install LAMMPS (optional, you can remove this line if you don't want to install it system-wide)
RUN make install

# Set the default command to run LAMMPS
CMD ["./lmp"]
