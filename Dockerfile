FROM python:3.8.3-buster
COPY . /data
WORKDIR /data
RUN pip install -r requirements.txt
CMD python ./main.py
