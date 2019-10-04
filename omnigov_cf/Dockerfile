FROM python:3.7.4-slim-buster
LABEL maintainer="Juan Becerra <juanbecerrawork@gmail.com>"

ENV INSTALL_PATH /omnigov_cf
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "omnigov_cf.app:create_app()"
