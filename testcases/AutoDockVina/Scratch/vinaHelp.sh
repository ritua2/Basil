#!/bin/bash

wget http://vina.scripps.edu/download/autodock_vina_1_1_2_linux_x86.tgz

tar -zxvf autodock_vina_1_1_2_linux_x86.tgz

cd autodock_vina_1_1_2_linux_x86/vina

# prepare Ligand and Receptor files if needed
# obabel ligand.pdb -O ligand.pdbqt
# obabel receptor.pdb -O receptor.pdbqt

./vina --help

rm ligand.pdbqt receptor.pdbqt
cd ..
rm autodock_vina_1_1_2_linux_x86.tgz
