# Use a base image with the necessary tools and libraries
FROM ubuntu:23.10

# Install required packages
RUN apt-get update && \
    apt-get install -y \
    wget \
    build-essential \
    ncbi-blast+

# Set the working directory inside the container
WORKDIR /

# Copy the sequence files into the container
COPY seq.fasta /seq.fasta
COPY query.fasta /query.fasta

# Define the entrypoint command
ENTRYPOINT ["blastp", "-query", "query.fasta", "-subject", "seq.fasta", "-out", "blast_results.txt", "-outfmt", "6"]
