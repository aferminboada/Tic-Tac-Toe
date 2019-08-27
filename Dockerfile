FROM python:3.6

RUN mkdir /vieja/
ADD . /vieja/
WORKDIR /vieja/
ENV PYTHONPATH /vieja/
