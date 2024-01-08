import random
import string
import sqlite3
from hashlib import sha256

# Constants for database and table names
DATABASE_NAME = 'passwords.db'
TABLE_NAME = 'passwords'

def connect_to_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        exit()

def create_passwords_table(cursor):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            password TEXT
        )
    ''')
    conn.commit()

def generate_password(length, use_special_chars, use_digits, use_lowercase_chars, use_uppercase_chars):
    characters = ''
    if use_lowercase_chars:
        characters += string.ascii_lowercase
    if use_uppercase_chars:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    if not characters:
        raise ValueError("No characters selected")
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def encrypt_password(password):
    hashed_password = sha256(password.encode()).hexdigest()
    return hashed_password

def save_password_to_database(cursor, encrypted_password):
    cursor.execute(f"INSERT INTO {TABLE_NAME} (password) VALUES (?)", (encrypted_password,))
    conn.commit()
    print("Password saved to the database.")

def get_confirmation(prompt):
    while True:
        try:
            response = input(prompt).lower()
            if response in ['y', 'n']:
                return response == 'y'
            else:
                print("Invalid input, please enter 'Y' or 'N'.")
        except ValueError:
            print("Invalid input, please enter 'Y' or 'N'.")

def get_valid_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Password length must be greater than zero.")
        except ValueError:
            print("Invalid input, please enter a valid number.")

def get_valid_chars():
    while True:
        use_special_chars = get_confirmation("Use special characters? Y/N ")
        use_digits = get_confirmation("Use digits? Y/N ")
        use_lowercase_chars = get_confirmation("Use lowercase characters? Y/N ")
        use_uppercase_chars = get_confirmation("Use uppercase characters? Y/N ")

        if any([use_lowercase_chars, use_uppercase_chars, use_special_chars, use_digits]):
            return use_special_chars, use_digits, use_lowercase_chars, use_uppercase_chars
        else:
            print("You must select at least one character type to generate a secure password!")

# Connect to the database and create passwords table
conn, cursor = connect_to_database()
create_passwords_table(cursor)

# Validate password length and character types selection
length = get_valid_length()
use_special_chars, use_digits, use_lowercase_chars, use_uppercase_chars = get_valid_chars()

# Generate and print the password
password = generate_password(length, use_special_chars, use_digits, use_lowercase_chars, use_uppercase_chars)
print(f"Generated password: {password}")

# Encrypt and save the password to the database
encrypted_password = encrypt_password(password)
save_password_to_database(cursor, encrypted_password)

# Close the database connection
conn.close()
