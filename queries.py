
import sqlite3
import csv
from pprint import pprint

sqlite_file = 'mydb.db'
connection = sqlite3.connect(sqlite_file)

cursor = connection.cursor()

# Drop the table if it already exists
cursor.execute("""
    DROP TABLE IF EXISTS nodes_tags
    """)
connection.commit()

cursor.execute("""
    CREATE TABLE nodes_tags(id INTEGER, key TEXT, value TEXT, type TEXT)
    """)
connection.commit()

# Read in data
with open('nodes_tags.csv', 'rb') as f:
    g = csv.DictReader(f)
    to_db = [(i['id'], i['key'], i['value'].decode('utf-8'), i['type']) for i in g]

# Insert data
cursor.executemany("""
    INSERT INTO nodes_tags(id, key, value, type) VALUES (?, ?, ?, ?);""",
    to_db)
connection.commit()

cursor.execute('SELECT COUNT(*) FROM nodes_tags;')
all_rows = cursor.fetchall()
print('1):')
pprint(all_rows)

connection.close()
