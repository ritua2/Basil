# Use an Ubuntu base image
FROM ubuntu:latest

# Set environment variables
ENV MV2_HOME=/opt/mvapich2
ENV OSU_VERSION=7.2

# Install required packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    wget \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

# Download and install MVAPICH2
RUN wget -qO- http://mvapich.cse.ohio-state.edu/download/mvapich/mv2/mvapich2-2.3.7.tar.gz | tar xz && \
    cd mvapich2-2.3.7 && \
    ./configure --prefix=$MV2_HOME && \
    make -j$(nproc) && \
    make install && \
    cd .. && rm -rf mvapich2-2.3.7

# Download and install OSU Micro-Benchmarks
RUN wget -qO- http://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-${OSU_VERSION}.tar.gz | tar xz && \
    cd osu-micro-benchmarks-${OSU_VERSION} && \
    ./configure CC=$MV2_HOME/bin/mpicc --prefix=/opt/osu && \
    make -j$(nproc) && \
    make install && \
    cd .. && rm -rf osu-micro-benchmarks-${OSU_VERSION}

# Create a directory for the MPI program and benchmarks
WORKDIR /mpi_app

# Copy the MPI program and benchmarks
COPY mpi_hello.c .
COPY osu-micro-benchmarks/ ./osu-micro-benchmarks/

# Compile the MPI program using MVAPICH2 compiler wrappers
RUN $MV2_HOME/bin/mpicc mpi_hello.c -o mpi_hello

# Run the OSU Micro-Benchmarks and the MPI program
CMD /opt/osu/bin/osu_latency && /opt/osu/bin/osu_bw && /opt/osu/bin/osu_bibw && /opt/osu/bin/osu_latency_mt && \
    mpirun -np 4 ./mpi_hello
