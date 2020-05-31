FROM python:3.8-alpine
MAINTAINER Fahim Ahmed Irfan

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache jpeg-dev
RUN apk --update add --no-cache --virtual .tmp-build-deps \
      gcc build-base libffi-dev freetype-dev libpng-dev openblas-dev linux-headers mysql-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

WORKDIR app
COPY . .

RUN adduser -D user
User user
EXPOSE 8000
