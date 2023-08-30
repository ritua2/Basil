FROM ubuntu:latest

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    mpich \
    openssh-server \
    wget \
    && rm -rf /var/lib/apt/lists/*

COPY mpi_hello.c /mpi_app/mpi_hello.c

RUN mpicc /mpi_app/mpi_hello.c -o /mpi_app/mpi_hello

COPY osu-micro-benchmarks-7.2.tar.gz /osu-micro-benchmarks-7.2.tar.gz

RUN tar xzf /osu-micro-benchmarks-7.2.tar.gz && \
    cd osu-micro-benchmarks-7.2 && \
    ./configure CC=mpicc CXX=mpicxx --prefix=/opt/osu && \
    make && \
    make install && \
    cd .. && rm -rf osu-micro-benchmarks-5.7.1

CMD mpirun -n 2 osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_latency && mpirun -n 2 osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_bw && mpirun -n 2 osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_bibw && mpirun -n 2 osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_latency_mt && mpirun -n 4 /mpi_app/mpi_hello
#CMD mpirun -n 2 osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_latency
