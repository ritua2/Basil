FROM ubuntu:23.10

WORKDIR /

COPY in.myinput /in.myinput

RUN apt-get update &&\
    apt-get install -y openmpi-bin libopenmpi-dev git build-essential cmake &&\
    git clone https://github.com/lammps/lammps.git ~/lammps &&\
    cd ~/lammps &&\
    mkdir build &&\
    cd build &&\
    cmake ../cmake -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_MPI=yes &&\
    make -j$(nproc) &&\
    make install &&\
    cd ~ &&\
    rm -rf ~/lammps

CMD  mpirun -np 4 --allow-run-as-root /usr/local/bin/lmp -in /in.myinput
