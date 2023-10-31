FROM python:3.9-slim-buster

MAINTAINER Md Mahmudulla Hassan <mhassan@miners.utep.edu>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt \
    && mkdir networks \
    && tar -xvf general.tar.gz -C networks/ \
    && tar -xvf refined.tar.gz -C networks/ \
    && tar -xvf mgltools_x86_64Linux2_1.5.6.tar.gz \
    && mv mgltools_x86_64Linux2_1.5.6 mgltools \
    && rm *.tar.gz \
    && cd mgltools \
    && ./install.sh \
    && echo "source /app/mgltools/initMGLtools.sh" >> ~/.bashrc

ENV PATH="/app/mgltools/bin:${PATH}"

ENTRYPOINT ["python3", "dlscore.py"]
