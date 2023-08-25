#!/bin/bash

# Set the installation directory
INSTALL_DIR=$HOME/namd_install

# Create the installation directory
mkdir -p $INSTALL_DIR

# Go to the installation directory
cd $INSTALL_DIR

# Download NAMD
wget https://charm.cs.illinois.edu/namd/2.15/download/819038/NAMD_2.15_Source.tar.gz

# Extract NAMD source
tar xvzf NAMD_2.15_Source.tar.gz

# Go into the NAMD source directory
cd NAMD_2.15_Source

# Build NAMD
./config Linux-x86_64-g++ --charm-arch multicore-linux-x86_64 --with-fftw3 --prefix $INSTALL_DIR
cd Linux-x86_64-g++
make -j$(nproc)

# Verify installation
if [ $? -eq 0 ]; then
    echo "NAMD installation successful"
else
    echo "NAMD installation failed"
    exit 1
fi

# Run NAMD help command
$INSTALL_DIR/NAMD_2.15_Source/Linux-x86_64-g++/namd2 +help

# Run water_simulation.namd
$INSTALL_DIR/NAMD_2.15_Source/Linux-x86_64-g++/namd2 water_simulation.namd
