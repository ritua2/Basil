FROM ubuntu:22.04

RUN apt update
RUN apt install -y git wget libxrender1

RUN mkdir -p ~/miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
RUN chmod +x ~/miniconda3/miniconda.sh
RUN ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
RUN rm -rf ~/miniconda3/miniconda.sh


RUN git clone --depth 1 https://github.com/sirimullalab/LigandNet.git
RUN ~/miniconda3/bin/conda env create -f LigandNet/environment.yml
CMD cd LigandNet/ && ~/miniconda3/bin/conda run -n ligandnet  python ligandnet.py --smiles CCCC --out .

