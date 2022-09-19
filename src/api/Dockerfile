FROM python:3.9.6-buster
ENV PYTHONBUFFERED=1
WORKDIR /src

RUN pip install poetry 

COPY pyproject.toml* poetry.lock* ./

RUN poetry config virtualenvs.in-project true
RUN if [-f pyproject.toml]; then poetry install; fi

ENTRYPOINT ["poetry","run","uvicorn","api.main:app","--host","0.0.0.0","--reload"]