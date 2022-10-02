FROM python:3.9.6-slim-buster

COPY public /usr/share/nginx/html/
WORKDIR /usr/share/nginx/html

RUN pip install --upgrade pip setuptools && \
    pip install streamlit pandas numpy matplotlib requests python-dotenv