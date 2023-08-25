FROM ubuntu:20.04

WORKDIR /root

ENV DEBIAN_FRONTEND=noninteractive

COPY testdata.tcl /root/testdata.tcl

RUN apt-get update && \
    apt-get install -y wget g++ && \
    rm -rf /var/lib/apt/lists/*
RUN wget https://opensees.berkeley.edu/OpenSees/user.opensees && \
    g++ -o OpenSees user.opensees && \
    rm user.opensees

ENTRYPOINT ["./OpenSees", "testdata.tcl"]
