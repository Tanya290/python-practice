#For PostgreSQL, you can use the psycopg2 library to connect to the database.
#INSTALLATION 
#pip install psycopg2

#CONNECTING TO PostgreSql:
import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    database='yourdatabase',
    user='yourusername',
    password='yourpassword'
)

# Create a cursor object
cursor = conn.cursor()

#CREATING A TABLE 
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
)
''')

# Commit the changes
conn.commit()

#INSERTING A TABLE 
cursor.execute('''
INSERT INTO users (name, age) VALUES (%s, %s)
''', ('Alice', 30))

# Commit the changes
conn.commit()


#QUERYING THE DATA 
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

#CLOSING THE CONNECTION
conn.close()