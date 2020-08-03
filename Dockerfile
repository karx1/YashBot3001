FROM python:3.8.5-buster
COPY . /data
WORKDIR /data
RUN pip install -r requirements.txt
ENV JISHAKU_NO_UNDERSCORE true
CMD python ./main.py
