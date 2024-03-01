apt update
apt install -y git wget bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
chmod +x ~/miniconda3/miniconda.sh
~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
PATH=~/miniconda3/bin:$PATH
git clone --depth 1 https://github.com/sirimullalab/LigandNet.git
cd LigandNet/ && ~/miniconda3/bin/conda env create -f environment.yml

~/miniconda3/bin/conda run -n ligandnet python LigandNet/ligandnet.py --smiles CCCC --out .