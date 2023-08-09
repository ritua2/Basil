FROM ubuntu:mantic

WORKDIR /
COPY test.c /test.c
RUN apt-get update &&\
    apt install -y gcc &&\
    gcc -o test test.c

CMD ["./test"]
