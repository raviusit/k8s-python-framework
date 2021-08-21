FROM python:3.9-slim-buster
LABEL maintainer="raviusit@gmail.com"
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ADD lib/ /lib
ADD run.py /run.py

CMD [ "python3", "./run.py" ]
