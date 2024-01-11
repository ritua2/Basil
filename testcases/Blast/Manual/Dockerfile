FROM ubuntu:23.10

WORKDIR /

COPY seq.fasta /seq.fasta
COPY query.fasta /query.fasta


RUN apt-get update && apt-get install -y wget build-essential ncbi-blast+

CMD blastp -query /query.fasta -subject /seq.fasta 