FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install poetry

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock /usr/src/app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /usr/src/app/

ENTRYPOINT [ "sh", "setup_django.sh" ]
CMD [ "gunicorn", "app_django.wsgi", "--bind", "0.0.0.0:8000", "--reload" ]
