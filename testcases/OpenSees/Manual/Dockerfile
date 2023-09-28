FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y wget g++

WORKDIR /root
RUN wget https://opensees.berkeley.edu/OpenSees/user.opensees && \
    g++ -o OpenSees user.opensees

COPY testdata.tcl /root/testdata.tcl

WORKDIR /root

CMD ["./OpenSees", "testdata.tcl"]
