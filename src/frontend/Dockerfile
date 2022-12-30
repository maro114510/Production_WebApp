FROM python:3.9.6-slim-buster

COPY streamlit /usr/share/nginx/html/streamlit/
WORKDIR /usr/share/nginx/html/streamlit/

RUN pip install --upgrade pip setuptools && \
    pip install streamlit requests python-dotenv


# End of Dockerfile