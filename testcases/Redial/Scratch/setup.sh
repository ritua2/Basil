apt update 
apt install -y git wget
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
PATH=~/miniconda3/bin:$PATH
git clone https://github.com/sirimullalab/redial-2020.git
cd redial-2020
~/miniconda3/bin/conda env create -f environment-redial-2020.yml

cd redial-2020/batch_screen && ~/miniconda3/bin/conda run -n redial-2020 python3 run_predictions.py --csvfile sample_data.csv --results .