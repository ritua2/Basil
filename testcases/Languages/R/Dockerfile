FROM debian:stable-slim

WORKDIR /

COPY test.R /test.R

RUN apt-get update &&\
    apt-get install -y r-base &&\
    apt-get clean

CMD ["Rscript", "test.R"]
