# base_os ubuntu:23.10

# Install required packages
apt-get update && apt-get install -y wget build-essential ncbi-blast+


#  the files 
#seq.fasta 
#query.fasta 
blastp -query /query.fasta -subject /seq.fasta 
