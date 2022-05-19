FROM python:3
ENV PYTHONUNBUFFERED=1

ENV DATABASE_URL=""
ENV AWS_KEY_ID="AKIAZRSVOEWWCKVTMXW2"
ENV AWS_SECRET_KEY="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"
ENV AWS_BUCKET="by-pets-test"

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/