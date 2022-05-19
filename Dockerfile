FROM python:3
ENV PYTHONUNBUFFERED=1

ENV DATABASE_URL=""
ENV AWS_KEY_ID=""
ENV AWS_SECRET_KEY=""
ENV AWS_BUCKET=""

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/