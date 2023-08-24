# Use a base image with necessary tools
FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    openmpi-bin \
    libopenmpi-dev \
    git

# Clone LAMMPS repository
RUN git clone https://github.com/lammps/lammps.git /opt/lammps

# Set the working directory inside the container
WORKDIR /opt/lammps

# Build LAMMPS with MPI support
RUN make mpi -j$(nproc)

# Set the default command to run LAMMPS help
CMD ["mpirun", "-np", "1", "lmp_mpi", "-h"]
