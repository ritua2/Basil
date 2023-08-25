#!/bin/bash

# Install required packages
sudo apt-get update
sudo apt-get install -y wget g++

# Download and install OpenSees
cd ~
wget https://opensees.berkeley.edu/OpenSees/user.opensees
g++ -o OpenSees user.opensees
rm user.opensees

# Copy the test data file to the home directory
cp /testdata.tcl ~/testdata.tcl

# Run OpenSees on testdata.tcl
./OpenSees testdata.tcl
