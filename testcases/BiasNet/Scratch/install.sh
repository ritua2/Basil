apt update
apt install -y git wget libxrender1 
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
chmod +x ~/miniconda3/miniconda.sh
~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
git clone --depth 1 https://github.com/sirimullalab/biasNet.git
cd biasNet/
~/miniconda3/bin/conda env create -f environment.yml
~/miniconda3/bin/conda activate biasnet
python3 run_biasnet.py --smiles "ClC1=CC=C(C=C1)C2=NOC3=C2CCNCC3"