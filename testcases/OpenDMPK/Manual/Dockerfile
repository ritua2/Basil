FROM ubuntu:22.04

RUN apt update
RUN apt install -y git wget

RUN mkdir -p ~/miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
RUN chmod +x ~/miniconda3/miniconda.sh
RUN ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
RUN rm -rf ~/miniconda3/miniconda.sh
ENV PATH ~/miniconda3/bin:$PATH
RUN ~/miniconda3/bin/conda init bash

RUN git clone --depth 1 https://github.com/Govindakc/openDMPK.git
RUN cd openDMPK/ 
RUN ~/miniconda3/bin/conda create -c conda-forge -n opendmpk rdkit==2018.09.1 
RUN ~/miniconda3/bin/conda run -n opendmpk pip install -r requirements.txt


CMD ~/miniconda3/bin/conda run -n opendmpk python run_opendmpk.py --smiles "OC(O)C(Cl)(Cl)Cl"
