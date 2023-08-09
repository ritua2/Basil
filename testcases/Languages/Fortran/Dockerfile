FROM ubuntu:23.10

WORKDIR /
COPY test.f90 /test.f90
RUN apt-get update &&\
    apt install -y gfortran &&\
    gfortran -o test test.f90

CMD ["./test"]
