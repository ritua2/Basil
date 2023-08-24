FROM ubuntu:latest

# Update package list and install required packages
RUN apt-get update && \
    apt-get install -y build-essential \
                       libboost-all-dev \
                       git \
                       wget \
                       && \
    rm -rf /var/lib/apt/lists/*

# Clone AutoDock Vina repository
RUN git clone https://github.com/ccsb-scripps/AutoDock-Vina /autodock-vina

# Build AutoDock Vina
RUN cd /autodock-vina/build/linux/release && \
    make

# Set the working directory
WORKDIR /autodock-vina/build/linux/release

# Run the vina -help command
CMD ["./vina", "-help"]
