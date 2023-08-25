# Use a base image with necessary tools
FROM ubuntu:latest

# Install required packages
RUN apt-get update && \
    apt-get install -y wget g++

# Download and install OpenSees
WORKDIR /
RUN wget https://opensees.berkeley.edu/OpenSees/user.opensees && \
    g++ -o OpenSees user.opensees

# Copy the test data file into the container
COPY testdata.tcl /testdata.tcl

# Run OpenSees on testdata.tcl
CMD ["./OpenSees", "testdata.tcl"]
