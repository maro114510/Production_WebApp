FROM python:3.9.6-slim-buster

COPY streamlit /usr/share/nginx/html/streamlit/
WORKDIR /usr/share/nginx/html/streamlit/

RUN pip install --upgrade pip setuptools && \
    pip install streamlit requests python-dotenv pandas numpy

# RUN apt install certbot python3-certbot-nginx systemd vim

# RUN apt update && \
# 	export DEBIAN_FRONTEND=noninteractive && \
# 	apt install -y tzdata && \
# 	ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
# 	dpkg-reconfigure --frontend noninteractive tzdata && \
# 	apt install -y nginx



# End of Dockerfile