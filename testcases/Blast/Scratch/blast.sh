#!/bin/bash

# NOTE: Make sure that you have downloaded ncbi-blast-2.14.1+-x64-linux.tar.gz or a similar file from https://ftp.ncbi.nlm.nih.gov/blast/executables/LATEST/

# Untar the file you have
tar zxvpf ncbi-blast-2.14.1+-x64-linux.tar.gz

# Export the 1st path
export PATH=$PATH:$HOME/ncbi-blast-2.14.1+/bin

# Verify
echo $PATH

# Make a directory to handle the databases
mkdir $HOME/blastdb

# Export the 2nd path
export BLASTDB=$HOME/blastdb

# Go to the database directory
cd $HOME/blastdb

# Get a database
perl /home/exouser/testing/Blast/Manual/ncbi-blast-2.14.1+/bin/update_blastdb.pl --passive --decompress 16S_ribosomal_RNA

# Check all files downloaded
ls -l

# Run help flag for verification
blastn -help

# Run version details for verification
blastn -version

# Setuo database for execution
blastdbcmd -db 16S_ribosomal_RNA -entry nr_025000 -out 16S_query.fa

# Run the database for verification
blastn -db 16S_ribosomal_RNA -query 16S_query.fa -task blastn -dust no -outfmt "7 delim=, qacc sacc evalue bitscore qcovus pident" -max_target_seqs 5

# Run seq.fasta and query.fasta 
blastn -db 16S_ribosomal_RNA -query /root/seq.fasta -out blast_output_seq.fasta
blastn -db 16S_ribosomal_RNA -query /root/query.fasta -out blast_output_query.fasta
