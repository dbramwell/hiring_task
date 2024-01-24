FROM python:3.12
WORKDIR /app
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY . /app
RUN poetry install --no-root