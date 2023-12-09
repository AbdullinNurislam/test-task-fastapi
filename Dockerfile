FROM python:3.10-slim

WORKDIR /srv

RUN pip install poetry

COPY poetry.lock pyproject.toml /srv/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY ./ /srv

CMD ["python", "main.py"]
