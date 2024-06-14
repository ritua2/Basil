# Use the latest version of Ubuntu
FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    git \
    cmake \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    g++ \
    libxerces-c-dev \
    libfox-1.6-dev \
    libgdal-dev \
    libproj-dev \
    libgl2ps-dev \
    swig

# Clone the SUMO repository
RUN git clone https://github.com/eclipse-sumo/sumo.git

# Set the working directory
WORKDIR /sumo

# Set the SUMO_HOME environment variable
ENV SUMO_HOME /sumo

# Build the SUMO project
RUN cmake -B build . && \
    cmake --build build -j2

# Default command
CMD ["bash"]