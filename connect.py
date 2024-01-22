import psycopg2

conn = psycopg2.connect(
    database="sample_db",
    user="jino",
    password="jino",
    host="localhost"
)

cur = conn.cursor()

cur.execute("SELECT * FROM student")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()

# from src.ml.predict import classifier
# classifier.predict_label([[5.1, 3.5, 1.4, 0.2]])