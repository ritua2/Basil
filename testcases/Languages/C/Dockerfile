FROM ubuntu:23.10

WORKDIR /
COPY test.c . .
RUN apt-get update &&\
    apt-get install -y gcc &&\
    gcc -o test test.c

CMD ["./test"]
