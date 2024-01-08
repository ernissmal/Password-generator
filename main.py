import tkinter as tk
from tkinter import messagebox
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
    messagebox.showinfo("Password Saved", "Password saved to the database.")

def generate_password_gui():
    length = length_slider.get()
    use_special_chars = special_char_var.get()
    use_digits = digit_var.get()
    use_lowercase_chars = lowercase_var.get()
    use_uppercase_chars = uppercase_var.get()

    try:
        password = generate_password(length, use_special_chars, use_digits, use_lowercase_chars, use_uppercase_chars)
        password_display.delete(1.0, tk.END)
        password_display.insert(tk.END, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def save_password_gui():
    encrypted_password = encrypt_password(password_display.get("1.0", tk.END).strip())
    save_password_to_database(cursor, encrypted_password)

def regenerate_password_gui():
    generate_password_gui()

# Connect to the database and create passwords table
conn, cursor = connect_to_database()
create_passwords_table(cursor)

# Create main window
app = tk.Tk()
app.title("Password Generator App")

# Title box
title_label = tk.Label(app, text="Password Generator", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=3)

# Information text box
info_label = tk.Label(app, text="Configure password options and generate or save passwords.", wraplength=300, justify=tk.LEFT)
info_label.grid(row=1, column=0, columnspan=3)

# Checkboxes
special_char_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()

special_char_check = tk.Checkbutton(app, text="Special Characters", variable=special_char_var)
digit_check = tk.Checkbutton(app, text="Digits", variable=digit_var)
lowercase_check = tk.Checkbutton(app, text="Lowercase Characters", variable=lowercase_var)
uppercase_check = tk.Checkbutton(app, text="Uppercase Characters", variable=uppercase_var)

special_char_check.grid(row=2, column=0)
digit_check.grid(row=2, column=1)
lowercase_check.grid(row=3, column=0)
uppercase_check.grid(row=3, column=1)

# Length slider
length_label = tk.Label(app, text="Password Length:")
length_slider = tk.Scale(app, from_=6, to=20, orient=tk.HORIZONTAL)
length_label.grid(row=4, column=0, sticky=tk.E)
length_slider.grid(row=4, column=1)

# Generate Password button
generate_button = tk.Button(app, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=5, column=0, columnspan=2)

# Display generated password
password_display = tk.Text(app, height=1, width=30)
password_display.grid(row=6, column=0, columnspan=2)

# Save on Database button
save_button = tk.Button(app, text="Save on Database", command=save_password_gui)
save_button.grid(row=7, column=0, columnspan=2)

# Regenerate button
regenerate_button = tk.Button(app, text="Regenerate", command=regenerate_password_gui)
regenerate_button.grid(row=8, column=0, columnspan=2)

# Run the Tkinter main loop
app.mainloop()

# Close the database connection
conn.close()
