FROM python:3.8-slim-buster


COPY requirements.txt /
#hadolint ignore=DL3013,DL3042

RUN  pip install --no-cache-dir -r requirements.txt

ENV PYTHONBUFFERED=1
WORKDIR /app/
COPY . /app/

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
