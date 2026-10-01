import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",    # replace with your actual password
    database="YOUR_DATABASE"  # replace with your actual database name
)

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")

tables = cursor.fetchall()
print("Connected successfully!")
print("Tables found:", tables)

cursor.close()
conn.close()