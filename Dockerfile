FROM python:2.7
MAINTAINER bandeep

RUN useradd test1

WORKDIR /home/test1

RUN chmod 777 /home/test1

USER test1

RUN pip install pytest
COPY isReverse.py .

