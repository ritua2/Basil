FROM ubuntu:23.10

WORKDIR /autodock-vina-build
ENV PATH /autodock-vina/build/linux/release:${PATH}

RUN apt-get update &&\
    apt-get install -y --no-install-recommends &&\
    apt-get install -y build-essential &&\
    apt-get install -y libboost-all-dev &&\
    apt-get install -y swig &&\
    apt-get install -y git &&\
    git config --global http.sslVerify false &&\
    git clone https://github.com/ccsb-scripps/AutoDock-Vina /autodock-vina &&\
    cd /autodock-vina &&\
    cd build/linux/release &&\
    make

CMD ["vina", "--help"]
