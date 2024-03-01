FROM ubuntu:22.04

WORKDIR /

RUN apt update &&\
    apt install -y git wget &&\
    mkdir -p ~/miniconda3 &&\
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh &&\
    chmod +x ~/miniconda3/miniconda.sh &&\
    ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3 &&\
    rm -rf ~/miniconda3/miniconda.sh &&\
    git clone --depth 1 https://github.com/sirimullalab/redial-2020.git &&\
    cd redial-2020 && ~/miniconda3/bin/conda env create -f environment-redial-2020.yml &&\
    mkdir /results

CMD  cd /redial-2020/batch_screen && ~/miniconda3/bin/conda run -n redial-2020 python3 run_predictions.py --csvfile $input_file --results /results
