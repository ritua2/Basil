FROM python:3.12-rc

WORKDIR /

COPY testpwf.py /testpwf.py

EXPOSE 5000

RUN apt-get update &&\
    pip install Flask

CMD ["python", "testpwf.py"]
