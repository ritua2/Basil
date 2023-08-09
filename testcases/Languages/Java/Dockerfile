FROM alpine:edge

WORKDIR /
COPY test.java /test.java
RUN apk update &&\
    apk add openjdk11 &&\
    apk add openjdk11-jre &&\
    javac test.java

CMD ["java", "test"]
