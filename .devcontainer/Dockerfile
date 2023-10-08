FROM python:3.10-alpine

RUN apk add --no-cache curl
RUN apk add --no-cache gcc
RUN apk add --no-cache git
RUN apk add --no-cache libffi-dev
RUN apk add --no-cache musl-dev

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/usr/local python3 -
