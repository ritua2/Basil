FROM ubuntu:20.04

WORKDIR /root

ENV DEBIAN_FRONTEND=noninteractive

COPY testdata.tcl /root/testdata.tcl

RUN apt-get update
RUN apt-get install -y wget g++
RUN rm -rf /var/lib/apt/lists/*
RUN wget https://opensees.berkeley.edu/OpenSees/user.opensees
RUN g++ -o OpenSees user.opensees
RUN rm user.opensees

ENTRYPOINT ["./OpenSees", "testdata.tcl"]
