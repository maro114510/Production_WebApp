FROM python:3.9.6

RUN apt-get update && \
	apt-get install -y cron \
	vim

RUN pip install --upgrade pip setuptools && \
	pip install requests