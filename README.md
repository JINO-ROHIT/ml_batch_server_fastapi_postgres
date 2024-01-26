# Batch Inference using Fastapi and Postgres

This project shows how to create a batch prediction setup using fastapi and postgres as a database.

## Project Overview

This project is designed for performing batch inference using a FastAPI web service for prediction, PostgreSQL as a database to store input data and predictions and ONNX Runtime for running the ml model. The system allows users to submit data for predictions through the FastAPI API, and the results are stored in a PostgreSQL database. A cron job is scheduled to run batch predictions at specific intervals during the day. Adminer is integrated to provide a user-friendly interface for database management.

## Installation

1. ### Build containers

```bash
make start
```

2. ### Check application health
```bash
curl -X 'GET' \
  'http://localhost:8000/health' \
  -H 'accept: application/json'
```

Response 
```json
{
  "health": "ok"
}

```

3. ### Call the predict api
```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[[0, 1, 2, 3]]'
```

Response 
```json
{
  "success": "data received for prediction!"
}

```

5. ### Manually trigger the batch prediction
```bash
curl -X 'POST' \
  'http://localhost:8000/predict_batch' \
  -H 'accept: application/json' \
  -d ''
```

Response 
```json
{
  "success": "batch prediction succesful!"
}
```

6. ### Stop the service

```bash
make stop
```
