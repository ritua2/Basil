FROM ubuntu:mantic

WORKDIR /
COPY test.java . .
RUN apt-get update &&\
    apt-get install -y openjdk-17-jdk &&\
    javac test.java

CMD ["java", "test"]
