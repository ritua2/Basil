#!/bin/bash

# Install required packages
sudo apt-get update
sudo apt-get install -y openmpi-bin libopenmpi-dev git

# Clone LAMMPS repository
git clone https://github.com/lammps/lammps.git ~/lammps

# Build LAMMPS with MPI support
cd ~/lammps
make mpi -j$(nproc)

# Display LAMMPS help
mpirun -np 1 ~/lammps/src/lmp_mpi -h

echo "MPI LAMMPS installation and help check completed."
