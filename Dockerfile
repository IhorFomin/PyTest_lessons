FROM python:3.8-alpine

ARG run_env
ENV wnv $run_env

LABEL "channel"="SolveMe"
LABEL "creator"="SolveMe community"

WORKDIR ./usr/lessons

COPY . .

RUN apk update && apk upgrade && apk add bash

RUN pip install pytest
RUN pip install faker
RUN pip install sqlalchemy
# RUN /bin/sh -c pip install psycopg2
# RUN /bin/sh -c pip install psycopg2
# RUN /bin/sh -c apt-get install -y python-psycopg2
RUN pip3 install psycopg2-binary
RUN pip install -r requirements.txt

CMD pytest -m "$env" -s -v tests/users/test_users.py
