FROM ubuntu:22.04

WORKDIR /

RUN apt update &&\
    apt install -y cmake python3 python3-pip g++ libxerces-c-dev libfox-1.6-dev libgdal-dev libproj-dev libgl2ps-dev swig git &&\
    git clone https://github.com/eclipse-sumo/sumo.git &&\
    cd sumo &&\
    export SUMO_HOME="$PWD" &&\
    export nproc=2 &&\
    cmake -B build . &&\
    cmake --build build -j$(nproc)
