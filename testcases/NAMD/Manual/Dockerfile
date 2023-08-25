# Use a base image with necessary tools
FROM ubuntu:latest

# Set the installation directory
ENV INSTALL_DIR /usr/local/namd

# Install required packages
RUN apt-get update && \
    apt-get install -y wget g++ fftw3 libfftw3-dev

# Download NAMD
WORKDIR /tmp
RUN wget https://charm.cs.illinois.edu/namd/2.15/download/819038/NAMD_2.15_Source.tar.gz && \
    tar xvzf NAMD_2.15_Source.tar.gz

# Build NAMD
WORKDIR /tmp/NAMD_2.15_Source
RUN ./config Linux-x86_64-g++ --charm-arch multicore-linux-x86_64 --with-fftw3 --prefix $INSTALL_DIR && \
    cd Linux-x86_64-g++ && \
    make -j$(nproc) && \
    make install

# Copy water_simulation.namd into the container
COPY water_simulation.namd /root/water_simulation.namd

# Set working directory
WORKDIR /root

# Run NAMD on water_simulation.namd
CMD ["$INSTALL_DIR/NAMD_2.15_Source/Linux-x86_64-g++/namd2", "water_simulation.namd"]
