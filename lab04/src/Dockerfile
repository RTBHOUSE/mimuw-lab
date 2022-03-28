FROM python:3.10-alpine

COPY requirements.txt main.py /code/

WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP main

# not a production grade app
CMD flask run
