FROM python:3.9-slim

ENV PROJECT_DIR code
WORKDIR /${PROJECT_DIR}
ADD ./requirements.txt /${PROJECT_DIR}/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && pip install --no-cache-dir -r requirements.txt

COPY ./src/ /${PROJECT_DIR}/src/
COPY ./models/ /${PROJECT_DIR}/models/
COPY ./configs/ /${PROJECT_DIR}/configs/