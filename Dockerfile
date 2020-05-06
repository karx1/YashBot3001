FROM python:slim-buster
COPY . /data
WORKDIR /data
RUN apt update && apt install gcc python3-dev -y && pip install -r requirements.txt
CMD python ./main.py
