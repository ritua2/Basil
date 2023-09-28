FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    git \
    wget \
    cmake \
    libopenmpi-dev \
    libboost-dev \
    liblammps-dev

RUN git clone https://github.com/namd/namd.git /namd

WORKDIR /namd

RUN cmake .

RUN make

CMD ./namd
