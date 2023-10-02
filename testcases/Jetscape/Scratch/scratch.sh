# Run this script as 'sudo ./scratch.sh', after 'chmod +x scratch.sh'

#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status.

# Environment Variables and Arguments
export DEBIAN_FRONTEND=noninteractive
ROOTSYS="/usr/local/root"
PATH="${ROOTSYS}/bin:${PATH}"
LD_LIBRARY_PATH="${ROOTSYS}/lib:${LD_LIBRARY_PATH}"
PYTHONPATH="${ROOTSYS}/lib"
username="jetscape-user"
JETSCAPE_DIR="/home/${username}/JETSCAPE"
SMASH_DIR="${JETSCAPE_DIR}/external_packages/smash/smash_code"
EIGEN3_ROOT="/usr/include/eigen3"
PYTHIA8DIR="/usr/local/"
PYTHIA8="/usr/local/"
PYTHIA8_ROOT_DIR="/usr/local/"
PATH="${PATH}:${PYTHIA8DIR}/bin"
id=1234

apt update && apt install -y \
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

apt update && apt install -y python3-pip

pip3 install --upgrade pip 
pip3 install \
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

mkdir -p "${ROOTSYS}" && mkdir -p "${HOME}/root"
(cd "${HOME}/root" && git clone --branch v6-26-06 --depth=1 https://github.com/root-project/root.git src)
(cd "${HOME}/root/src" && mkdir -p build && cd build && cmake ../src -DCMAKE_CXX_STANDARD=14 -DCMAKE_INSTALL_PREFIX=${ROOTSYS} && make -j4 install)
rm -r "${HOME}/root"

(curl -SL http://hepmc.web.cern.ch/hepmc/releases/HepMC3-3.2.5.tar.gz | tar -xvzC /usr/local)
(cd /usr/local && mkdir -p hepmc3-build && cd hepmc3-build && cmake ../HepMC3-3.2.5 -DCMAKE_INSTALL_PREFIX=/usr/local -DHEPMC3_ENABLE_ROOTIO=ON -DROOT_DIR=${ROOTSYS} -DHEPMC3_BUILD_EXAMPLES=ON && make -j4 install)
rm -r /usr/local/hepmc3-build

pythiaV="8309"
(curl -SLk http://pythia.org/download/pythia83/pythia${pythiaV}.tgz | tar -xvzC /usr/local)
(cd /usr/local/pythia${pythiaV} && ./configure --enable-shared --prefix=/usr/local/ --with-hepmc3=/usr/local/HepMC3-3.2.5 && make -j4 && make -j4 install)

(cd / && git clone --depth 1 --branch v1.3.8.8 https://github.com/matplo/heppy.git)
(cd heppy && ./external/fastjet/build.sh && ./external/hepmc2/build.sh && ./cpptools/build.sh)

(curl -SLk https://sourceforge.net/projects/modules/files/Modules/modules-4.5.1/modules-4.5.1.tar.gz | tar -xvzC /usr/local)
(cd /usr/local/modules-4.5.1 && ./configure --prefix=/usr/local --modulefilesdir=/heppy/modules && make -j4 && make -j4 install)

groupadd -g ${id} ${username}
useradd --create-home --home-dir /home/${username} -u ${id} -g ${username} ${username}

echo "Script finished successfully!"
