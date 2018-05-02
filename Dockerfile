FROM python:latest

ADD . /app

WORKDIR /app
ENTRYPOINT [ "python", "dockertest.py" ]
CMD ["$@"]