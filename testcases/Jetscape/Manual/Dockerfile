# This file was used as a testcase for BASIL, it was found at https://github.com/JETSCAPE/JETSCAPE/blob/main/docker/Dockerfile.base

FROM ubuntu:focal
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y \
doxygen \
emacs \
ffmpeg \
gsl-bin \
hdf5-tools \
less \
libboost-all-dev \
libeigen3-dev \
libgsl-dev \
libhdf5-serial-dev \
libxpm-dev \
openmpi-bin \
rsync \
swig \
valgrind \
git \
vim \
build-essential \
cmake \
wget \
curl \
tclsh \
tcl-dev \
libxft-dev \
libxext-dev \
libfftw3-3 \
&& rm -rf /var/lib/apt/lists/*

RUN apt update && apt install -y python3-pip

RUN pip3 install --upgrade pip 
RUN pip3 install \
emcee==2.2.1 \
h5py \
hic \
hsluv \
jupyter \
matplotlib \
nbdime \
numpy \
pandas \
pathlib \
ptemcee \
pyhepmc \
pyyaml \
scikit-learn \
scipy \
seaborn \
tqdm

ENV ROOTSYS="/usr/local/root"
ENV PATH="${ROOTSYS}/bin:${PATH}"
ENV LD_LIBRARY_PATH="${ROOTSYS}/lib:${LD_LIBRARY_PATH}"
ENV PYTHONPATH="${ROOTSYS}/lib"

RUN mkdir -p ${ROOTSYS} && mkdir -p ${HOME}/root
RUN cd ${HOME}/root && git clone --branch v6-26-06 --depth=1 https://github.com/root-project/root.git src
RUN cd ${HOME}/root/src && mkdir build && cd build
RUN cmake ../src -DCMAKE_CXX_STANDARD=14 -DCMAKE_INSTALL_PREFIX=${ROOTSYS}
RUN make -j4 install
RUN rm -r ${HOME}/root

RUN curl -SL http://hepmc.web.cern.ch/hepmc/releases/HepMC3-3.2.5.tar.gz | tar -xvzC /usr/local
RUN cd /usr/local && mkdir hepmc3-build && cd hepmc3-build
RUN cmake ../HepMC3-3.2.5 -DCMAKE_INSTALL_PREFIX=/usr/local -DHEPMC3_ENABLE_ROOTIO=ON -DROOT_DIR=${ROOTSYS} -DHEPMC3_BUILD_EXAMPLES=ON
RUN make -j4 install 
RUN rm -r /usr/local/hepmc3-build

ARG pythiaV="8309"
RUN curl -SLk http://pythia.org/download/pythia83/pythia${pythiaV}.tgz | tar -xvzC /usr/local
RUN cd /usr/local/pythia${pythiaV}
RUN ./configure --enable-shared --prefix=/usr/local/ --with-hepmc3=/usr/local/HepMC3-3.2.5
RUN make -j4
RUN make -j4 install

ARG username=jetscape-user
ENV JETSCAPE_DIR="/home/${username}/JETSCAPE"
ENV SMASH_DIR="${JETSCAPE_DIR}/external_packages/smash/smash_code"
ENV EIGEN3_ROOT /usr/include/eigen3
ENV PYTHIA8DIR /usr/local/
ENV PYTHIA8 /usr/local/
ENV PYTHIA8_ROOT_DIR /usr/local/
ENV PATH $PATH:$PYTHIA8DIR/bin

RUN cd / && git clone --depth 1 --branch v1.3.8.8 https://github.com/matplo/heppy.git
RUN cd heppy && ./external/fastjet/build.sh
RUN cd heppy && ./external/hepmc2/build.sh
RUN cd heppy && ./cpptools/build.sh

RUN curl -SLk https://sourceforge.net/projects/modules/files/Modules/modules-4.5.1/modules-4.5.1.tar.gz | tar -xvzC /usr/local
RUN cd /usr/local/modules-4.5.1
RUN ./configure --prefix=/usr/local --modulefilesdir=/heppy/modules
RUN make -j4
RUN make -j4 install

ARG id=1234
RUN groupadd -g ${id} ${username}
RUN useradd --create-home --home-dir /home/${username} -u ${id} -g ${username} ${username}
USER ${username}
ENV HOME /home/${username}
WORKDIR ${HOME}

ENTRYPOINT /bin/bash
