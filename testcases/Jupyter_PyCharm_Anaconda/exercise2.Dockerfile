FROM continuumio/anaconda3

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install jupyter && \
    wget https://download-cf.jetbrains.com/python/pycharm-community-2023.1.tar.gz && \
    tar -xvzf pycharm-community-2023.1.tar.gz && \
    rm pycharm-community-2023.1.tar.gz && \
    echo "export PATH=\$PATH:/opt/pycharm-community-2023.1/bin" >> ~/.bashrc

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
