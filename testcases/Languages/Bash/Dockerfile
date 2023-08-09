FROM alpine:edge

WORKDIR /
COPY test.sh /test.sh
RUN apk update &&\
    apk add bash &&\
    chmod +x /test.sh

CMD ["/bin/bash", "/test.sh"]
