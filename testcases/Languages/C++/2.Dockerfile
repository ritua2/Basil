FROM debian:stable-backports

WORKDIR /
COPY test.cpp /test.cpp
RUN apt-get update &&\
    apt install -y g++ &&\
    g++ -o test test.cpp

CMD ["./test"]
