FROM ubuntu:22.04

RUN apt update
RUN apt install -y git wget

RUN mkdir -p ~/miniconda3
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
RUN chmod +x ~/miniconda3/miniconda.sh
RUN ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
RUN rm -rf ~/miniconda3/miniconda.sh
ENV PATH ~/miniconda3/bin:$PATH
RUN conda init bash

RUN git clone --depth 1 https://github.com/sirimullalab/redial-2020.git
RUN cd redial-2020 && ~/miniconda3/bin/conda env create -f environment-redial-2020.yml
CMD cd batch_screen && ~/miniconda3/bin/conda run -n redial-2020 python3 run_predictions.py --csvfile sample_data.csv --results .