# Use the base image
FROM ubuntu:20.04

# Update the package repository, install Python, dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    default-jdk \
    libxrender1 \
    libxtst6 \
    libxi6

# Install PyCharm latest ver
RUN wget -O /tmp/pycharm.tar.gz https://download.jetbrains.com/python/pycharm-community-2023.1.tar.gz && \
    tar -xzf /tmp/pycharm.tar.gz -C /opt && \
    rm /tmp/pycharm.tar.gz && \
    ln -s /opt/pycharm-community-2023.1/bin/pycharm.sh /usr/local/bin/pycharm

# Set environment variables
ENV DISPLAY=:0
ENV TZ=UTC

# Set the entry point
ENTRYPOINT [ "pycharm" ]
