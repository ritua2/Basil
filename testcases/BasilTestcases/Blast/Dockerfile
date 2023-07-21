# Use a base image that includes BLAST and necessary tools
FROM ubuntu

# Set the working directory inside the container
WORKDIR /blast_db

# Copy the sequence file into the container
COPY seq.fasta .

RUN apt-get update
RUN apt-get install -y ncbi-blast+
# Create the BLAST database
RUN makeblastdb -in seq.fasta -dbtype nucl -parse_seqids

# Specify the command to run BLAST
CMD ["blastn", "-db", "seq.fasta", "-query", "query.fasta", "-out", "results.txt", "-outfmt", "6"]
