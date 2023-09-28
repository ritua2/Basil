#!/bin/bash

# Install required packages
sudo apt-get update
sudo apt-get install -y openmpi-bin libopenmpi-dev git

# Clone LAMMPS repository
git clone https://github.com/lammps/lammps.git ~/lammps

# Set the working directory
cd ~/lammps

# Build LAMMPS with MPI support
make mpi -j$(nproc)

# Verify installation
if [ $? -eq 0 ]; then
    echo "LAMMPS installation successful"
else
    echo "LAMMPS installation failed"
    exit 1
fi

# Copy your input file to the working directory
cp in.myinput ~/lammps/in.myinput

# Run LAMMPS with your input file using 4 MPI processes
mpirun -np 4 ~/lammps/src/lmp_mpi -in in.myinput
