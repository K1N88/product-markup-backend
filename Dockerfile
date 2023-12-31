FROM python:3.10-slim
WORKDIR /prosept_app
COPY ./requirements.txt .
COPY ./requirementsc.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install -r requirementsc.txt --no-cache-dir
COPY app app
COPY alembic alembic
COPY csv csv
COPY alembic.ini .
