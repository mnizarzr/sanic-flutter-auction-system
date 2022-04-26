ARG PYTHON_VERSION=3.10.0
ARG POETRY_VERSION=1.1.11

FROM python:$PYTHON_VERSION

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1
ENV \
    POETRY_VERSION=$POETRY_VERSION \
    POETRY_HOME="/opt/poetry"

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app/

COPY *.lock *.toml ./

RUN poetry install

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "/app/server.py"]