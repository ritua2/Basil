#!/bin/bash

echo "Running the setup and building AutoDock Vina w/o Boost..."

sudo apt-get update

sudo apt-get install -y build-essential

sudo apt-get install -y libboost-all-dev swig

git clone https://github.com/ccsb-scripps/AutoDock-Vina

cd AutoDock-Vina/build/linux/release

make

echo "Setup and build completed successfully."

echo "Running Vina now..."

vina --config /home/exouser/testing/AutoDock-Vina/testautovina/conf.txt
