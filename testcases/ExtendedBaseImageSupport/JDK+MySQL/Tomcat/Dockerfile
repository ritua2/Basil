FROM tomcat

WORKDIR /MIDAS
ENV c1 test
ENV c2 test2

ENV d1 sample1
ENV d2 sample2

COPY sample-input.midas.json .
COPY sample-input.midas.json /MIDAS/MIDAS/sample-input.midas.json
RUN apt-get update && apt-get upgrade -y &&\
    apt-get install -y python3 gcc &&\
    apt-get install -y curl &&\
    apt-get install -y wget

CMD ["echo", "'Meow~Meow~'"]
