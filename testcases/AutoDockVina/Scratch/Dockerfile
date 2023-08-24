FROM ubuntu:kinetic

WORKDIR /

COPY conf.txt /conf.txt

COPY ligand.pdbqt /ligand.pdbqt

COPY protein.pdbqt /protein.pdbqt

RUN apt-get update &&\
    apt-get install -y build-essential &&\
    apt-get install -y libboost-all-dev swig git &&\
    git clone https://github.com/ccsb-scripps/AutoDock-Vina /autodock-vina &&\
    cd autodock-vina/build/linux/release &&\
    make

CMD ["autodock-vina/build/linux/release/vina", "--config", "conf.txt"]
