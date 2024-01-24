import psycopg2
from psycopg2 import sql
import json
from datetime import datetime
from typing import List
from loguru import logger

from src.db.connect import conn
from src.ml.predict import classifier

def create_entry(values: List[List[float]]):
    cur = conn.cursor()

    list_of_lists = values
    prediction_value = "NA"
    current_timestamp = datetime.now()

    insert_query = sql.SQL("""
        INSERT INTO iris_predictions (values, prediction, timestamp)
        VALUES (%s, %s, %s)
    """)

    with conn.cursor() as cursor:
        cursor.execute(insert_query, (json.dumps(list_of_lists), prediction_value, current_timestamp))

    conn.commit()
    #conn.close()


def retrieve_all():
    cur = conn.cursor()

    select_query = sql.SQL("""
    SELECT * FROM iris_predictions
    """)

    with conn.cursor() as cursor:
        cursor.execute(select_query)
        rows = cursor.fetchall()

    for row in rows:
        values_json, prediction, timestamp = row
        values_list = json.loads(str(values_json))
        logger.info(f"Values: {values_list}, Prediction: {prediction}, Timestamp: {timestamp}")

    #conn.close()

def predict_all():
    cur = conn.cursor()

    select_query = sql.SQL("""
    SELECT * FROM iris_predictions
    WHERE prediction = 'NA'
    """)

    with conn.cursor() as cursor:
        cursor.execute(select_query)
        rows = cursor.fetchall()

    for row in rows:
        values_json, current_prediction, timestamp = row
        values_list = json.loads(str(values_json))

        print(values_list)
        new_prediction = classifier.predict_label(values_list)

        update_query = sql.SQL("""
            UPDATE iris_predictions
            SET prediction = %s
            WHERE timestamp = %s
        """)

        with conn.cursor() as cursor:
            cursor.execute(update_query, (new_prediction, timestamp))

        #logger.success(f"Values: {values_list}, Old Prediction: {current_prediction}, New Prediction: {new_prediction}, Timestamp: {timestamp}")

    conn.commit()
    #conn.close()


def remove_all():
    delete_query = sql.SQL("""
    DELETE FROM iris_predictions
    """)

    with conn.cursor() as cursor:
        cursor.execute(delete_query)

    conn.commit()
    #conn.close()