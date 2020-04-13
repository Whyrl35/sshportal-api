# docker build -t sshportal-api:v0.1 .
# clone new repo, build image, (no db, no conf)
# env for conf or read from external
# db read from external
FROM python:3.7-slim-buster

RUN pip install --upgrade pip && \
    pip install virtualenv

COPY . /app

WORKDIR /app

RUN virtualenv -p python3 venv

ENV PATH="/app/venv/bin:$PATH"

RUN . venv/bin/activate && \
    pip install -r requirements.txt

VOLUME ["/data"]

ENV CONF_PATH="/data"

EXPOSE 8000

ENTRYPOINT [ "gunicorn" ]
CMD [ "--bind", "0.0.0.0:8000", "run:app" ]
