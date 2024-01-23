import psycopg2
from psycopg2 import sql
import json
from datetime import datetime

conn = psycopg2.connect(
    database="sample_db",
    user="jino",
    password="jino",
    host="localhost"
)

# from src.ml.predict import classifier
# classifier.predict_label([[5.1, 3.5, 1.4, 0.2]])