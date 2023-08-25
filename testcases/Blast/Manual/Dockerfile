FROM ubuntu:latest

RUN apt-get update 

RUN apt-get install -y wget ncbi-blast+

WORKDIR /

ENTRYPOINT ["blastp", "-help"]
