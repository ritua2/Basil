#!/bin/bash

# Install BLAST
sudo apt-get update
sudo apt-get install -y ncbi-blast+

# Run BLAST with the help flag
blastp -help

echo "BLAST installation has been verified by running the HELP flag..."
