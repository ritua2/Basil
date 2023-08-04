FROM debian:stable

WORKDIR /
COPY test.cpp . .
RUN apt-get update &&\
    apt-get install -y g++ &&\
    rm -rf /var/lib/apt/lists/* &&\
    g++ -o test test.cpp

CMD ["./test"]
