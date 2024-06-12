#SQLite
#SQLite is a self-contained, serverless, and zero-configuration database engine.
#Python comes with built-in support for SQLite via the sqlite3 module.'''

#Connecting to SQLite:
import sqlite3

# Connect to a SQLite database or create it if it doesn't exist
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

#Creating a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

# Commit the changes
conn.commit()

#INSERTING VALUES INTO THE TABLE 
cursor.execute('''
INSERT INTO users (name, age) VALUES (?, ?)
''', ('Alice', 30))

# Commit the changes
conn.commit()

#QUERING DATA INTO THE TABLE 
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

#UPDATING DATA INTO THE TABLE
cursor.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (32, 'Alice'))
conn.commit()

#DELETING DATA INTO THE TABLE 
cursor.execute('''
DELETE FROM users WHERE name = ?
''', ('Alice',))
conn.commit()

#CLOSING THE CONNECTION 
cursor.close()
conn.close()