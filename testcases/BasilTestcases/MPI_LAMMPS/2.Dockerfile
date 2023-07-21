# Use Ubuntu as the base image
FROM ubuntu:latest

# Set non-root user and group
ARG USERNAME=lammpsuser
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Install prerequisites and update package information
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    mpi-default-bin \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID --create-home --shell /bin/bash $USERNAME

# Switch to the non-root user
USER $USERNAME

# Set the working directory in the non-root user's home directory
WORKDIR /home/$USERNAME

# Install additional dependencies (if needed) using the non-root user
# For example, if you need to install git and cmake, uncomment the lines below:
# RUN sudo apt-get update && \
#     sudo apt-get install -y git cmake

# Clone and build MPI LAMMPS using the non-root user
RUN git clone -b stable https://github.com/lammps/lammps.git /home/$USERNAME/lammps && \
    cd /home/$USERNAME/lammps && \
    mkdir build && \
    cd build && \
    cmake ../cmake -DPKG_MPI=yes && \
    make -j$(nproc)

# Set the default command to run the help flag
CMD ["mpirun", "-np", "4", "/home/$USERNAME/lammps/build/lmp_mpi", "-h"]
