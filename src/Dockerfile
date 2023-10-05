FROM ubuntu:16.04

ENV LC_ALL C
ENV PATH /usr/games

RUN apt-get update &&\
    apt-get install -y fortune &&\
    apt-get install -y cowsay &&\
    apt-get install -y lolcat &&\
    apt-get install -y python3-pip

CMD ["fortune", "|", "cowsay", "|", "lolcat"]
