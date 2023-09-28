# Use a base image with MPI and necessary tools
FROM ubuntu:23.10

# Install required packages
RUN apt-get update && \
    apt-get install -y openmpi-bin libopenmpi-dev git g++

# Clone LAMMPS repository
RUN git clone https://github.com/lammps/lammps.git /opt/lammps

# Set the working directory inside the container
WORKDIR /opt/lammps

# Build LAMMPS with MPI support
RUN make yes-all && \
    make mpi -j$(nproc)

# Set the default command to run LAMMPS
CMD ["mpirun", "-np", "4", "lmp_mpi", "-in", "in.myinput"]
