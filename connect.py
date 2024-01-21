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