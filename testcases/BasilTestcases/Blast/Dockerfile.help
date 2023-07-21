FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y ncbi-blast+

COPY seq_db.* /blast/db/

CMD ["blastn","-help"]
