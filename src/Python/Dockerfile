FROM ubuntu:focal
ARG DEBIAN_FRONTEND=noninteractive
ARG username=jetscape-user
ARG pythiaV="8309"
ARG id=1234

ENV ROOTSYS="/usr/local/root" \
    PATH="/usr/local/root/bin:$PATH:$PYTHIA8DIR/bin" \
    LD_LIBRARY_PATH="/usr/local/lib:/usr/local/root/lib:$LD_LIBRARY_PATH" \
    PYTHONPATH="/usr/local/root/lib" \
    JETSCAPE_DIR="/home/${username}/JETSCAPE" \
    SMASH_DIR="${JETSCAPE_DIR}/external_packages/smash/smash_code" \
    EIGEN3_ROOT="/usr/include/eigen3" \
    PYTHIA8DIR="/usr/local/" \
    PYTHIA8="/usr/local/" \
    PYTHIA8_ROOT_DIR="/usr/local/"

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
python3-pip \
&& rm -rf /var/lib/apt/lists/* \
&& pip3 install --upgrade pip \
&& pip3 install \
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

RUN mkdir -p ${ROOTSYS} && mkdir -p ${HOME}/root && cd ${HOME}/root \
&& git clone --branch v6-26-06 --depth=1 https://github.com/root-project/root.git src \
&& mkdir build && cd build \
&& cmake ../src -DCMAKE_CXX_STANDARD=14 -DCMAKE_INSTALL_PREFIX=${ROOTSYS} \
&& make -j8 install \
&& rm -r ${HOME}/root \
&& curl -SL http://hepmc.web.cern.ch/hepmc/releases/HepMC3-3.2.5.tar.gz | tar -xvzC /usr/local \
&& cd /usr/local \
&& mkdir hepmc3-build \
&& cd hepmc3-build \
&& cmake ../HepMC3-3.2.5 -DCMAKE_INSTALL_PREFIX=/usr/local -DHEPMC3_ENABLE_ROOTIO=ON -DROOT_DIR=${ROOTSYS} -DHEPMC3_BUILD_EXAMPLES=ON \
&& make -j8 install \
&& rm -r /usr/local/hepmc3-build

RUN curl -SLk http://pythia.org/download/pythia83/pythia${pythiaV}.tgz \
| tar -xvzC /usr/local \
&& cd /usr/local/pythia${pythiaV} \
&& ./configure --enable-shared --prefix=/usr/local/ --with-hepmc3=/usr/local/HepMC3-3.2.5 \
&& make -j8 \
&& make -j8 install

RUN cd / \
&& git clone --depth 1 --branch v1.3.8.8 https://github.com/matplo/heppy.git \
&& cd heppy \
&& ./external/fastjet/build.sh \
&& ./external/hepmc2/build.sh \
&& ./cpptools/build.sh \
&& curl -SLk https://sourceforge.net/projects/modules/files/Modules/modules-4.5.1/modules-4.5.1.tar.gz \
| tar -xvzC /usr/local \
&& cd /usr/local/modules-4.5.1 \
&& ./configure --prefix=/usr/local --modulefilesdir=/heppy/modules \
&& make -j8 \
&& make -j8 install

RUN groupadd -g ${id} ${username} \
&& useradd --create-home --home-dir /home/${username} -u ${id} -g ${username} ${username}
USER ${username}
ENV HOME /home/${username}
WORKDIR ${HOME}

ENTRYPOINT ["/bin/bash"]
