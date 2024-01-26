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