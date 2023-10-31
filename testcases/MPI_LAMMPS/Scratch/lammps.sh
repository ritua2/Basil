#!/bin/bash

# Update the package manager
sudo apt-get update

# Install required packages and dependencies
sudo apt-get install -y openmpi-bin libopenmpi-dev git build-essential cmake

# Clone LAMMPS repository
git clone https://github.com/lammps/lammps.git ~/lammps

# Set the working directory
cd ~/lammps

# Create a build directory
mkdir build
cd build

# Configure LAMMPS with MPI support
cmake ../cmake -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_MPI=yes

# Build LAMMPS
make -j$(nproc)

# Install LAMMPS
sudo make install

# Verify installation
if [ $? -eq 0 ]; then
    echo "LAMMPS installation successful"
else
    echo "LAMMPS installation failed"
    exit 1
fi

# Clean up
cd ~
rm -rf ~/lammps

# Run LAMMPS with your input file using 4 MPI processes
mpirun -np 4 /usr/local/bin/lmp -in /home/exouser/in.myinput
