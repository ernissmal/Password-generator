import sqlite3

DATABASE_FILE = 'passwords.db'

def init_db():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def save_password(name, password):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO passwords (name, password) VALUES (?, ?)', (name, password))
        conn.commit()

def get_passwords():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT name, password FROM passwords')
        return cursor.fetchall()

# Initialize the database
init_db()
