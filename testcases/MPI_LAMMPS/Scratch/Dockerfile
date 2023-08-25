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

# Copy your input file into the container
COPY in.myinput /opt/lammps/in.myinput

# Set the default command to run LAMMPS with your input file
CMD ["mpirun", "-np", "4", "lmp_mpi", "-in", "in.myinput"]
