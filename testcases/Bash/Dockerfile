FROM ubuntu:23.10

WORKDIR /
COPY test.sh /test.sh
RUN apt-get update &&\
    apt install -y bash &&\
    chmod +x /test.sh

ENTRYPOINT ["/bin/bash", "/test.sh"]

CMD ["factorial(5)"]
