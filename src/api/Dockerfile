FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry

RUN apt-get update && \
	apt-get install -y cron \
	vim \
	which \
	git

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi

ENTRYPOINT [ "poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload" ]


# End of Dockerfile