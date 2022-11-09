FROM centos:7

WORKDIR /MIDAS
ENV c2 test2
ENV c1 test

ENV d1 sample1
ENV d2 sample2

COPY sample-input.midas.json .
COPY sample-input.midas.json /MIDAS/MIDAS/sample-input.midas.json
RUN yum install -y python python3 gcc &&\
    yum install -y curl &&\
    yum install -y wget

CMD ["echo", "'Hello", "world'"]
