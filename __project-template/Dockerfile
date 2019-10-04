FROM python:3.7.4-slim-buster
MAINTAINER Juan Becerra <juanbecerrawork@gmail.com>

ENV INSTALL_PATH /__project-template
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "__project-template.app:create_app()"
