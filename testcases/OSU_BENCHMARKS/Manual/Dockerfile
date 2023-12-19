FROM ubuntu:latest

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    mpich \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

COPY mpi_hello.c /mpi_app/mpi_hello.c

RUN mpicc /mpi_app/mpi_hello.c -o /mpi_app/mpi_hello

CMD mpirun --help && mpiexec -n 4 /mpi_app/mpi_hello
