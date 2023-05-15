#Exercise 1
FROM python:3.12-rc-bullseye

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
    curl \
    --no-install-recommends \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir networks \
    && curl -o general.tar.gz https://drugdiscovery.utep.edu/download.php?file=general-10.tar.gz \
    && curl -o refined.tar.gz https://drugdiscovery.utep.edu/download.php?file=refined-10.tar.gz \
    && tar -xvf general.tar.gz && mv general networks/ && rm -f general.tar.gz \
    && tar -xvf refined.tar.gz && mv refined networks/ && rm -f refined.tar.gz

RUN curl -O http://mgltools.scripps.edu/downloads/downloads/tars/releases/REL1.5.6/mgltools_x86_64Linux2_1.5.6.tar.gz \
    && tar -xvf mgltools_x86_64Linux2_1.5.6.tar.gz && rm mgltools_x86_64Linux2_1.5.6.tar.gz \
    && cd /app/mgltools_x86_64Linux2_1.5.6 \
    && ./install.sh \
    && rm -rf *.gz \
    && echo "source /app/mgltools_x86_64Linux2_1.5.6/initMGLtools.sh" >> ~/.bashrc

ENV DISPLAY=:0
ENV TZ=UTC

ENV PATH="/app/mgltools_x86_64Linux2_1.5.6/bin:${PATH}"

ENTRYPOINT ["python", "dlscore.py"]
