FROM ubuntu:23.10

WORKDIR /

COPY mpi_hello.c /mpi_hello.c
COPY osu-micro-benchmarks-7.2.tar.gz /osu-micro-benchmarks-7.2.tar.gz
COPY LICENSE.txt ./LICENSE

RUN apt-get update && 
DEBIAN_FRONTEND=noninteractive apt-get install -y 
build-essential 
mpich 
openssh-server 
wget && 
rm -rf /var/lib/apt/lists/*

RUN mpicc /mpi_hello.c -o /mpi_hello

RUN tar xzf /osu-micro-benchmarks-7.2.tar.gz && 
cd osu-micro-benchmarks-7.2 && 
./configure CC=mpicc CXX=mpicxx && 
make && 
make install

CMD ["mpirun", "-n", "2", "osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_latency", "mpirun", "-n", "2", "osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_bw", "mpirun", "-n", "2", "osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_bibw", "mpirun", "-n", "2", "osu-micro-benchmarks-7.2/c/mpi/pt2pt/standard/osu_latency_mt", "mpirun", "-n", "4", "/mpi_hello"]
