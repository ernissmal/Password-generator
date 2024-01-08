import tkinter as tk
from tkinter import ttk, messagebox
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

def decrypt_password(encrypted_password):
    # For demonstration purposes, decryption is just reversing the encryption
    return encrypted_password[::-1]

def save_password_to_database(cursor, encrypted_password):
    cursor.execute(f"INSERT INTO {TABLE_NAME} (password) VALUES (?)", (encrypted_password,))
    conn.commit()
    messagebox.showinfo("Password Saved", "Password saved to the database.")

def fetch_passwords_from_database(cursor):
    cursor.execute(f"SELECT password FROM {TABLE_NAME}")
    passwords = cursor.fetchall()
    return passwords

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
        info_label.config(text="Password generated successfully! Save it to the database and copy or regenerate it!")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def save_password_gui():
    password = password_display.get("1.0", tk.END).strip()
    if password:
        encrypted_password = encrypt_password(password)
        save_password_to_database(cursor, encrypted_password)
        info_label.config(text="Password saved to the database.")
    else:
        messagebox.showwarning("Empty Password", "Please generate a password before saving.")

def fetch_passwords_gui():
    passwords = fetch_passwords_from_database(cursor)
    passwords_display.delete(1.0, tk.END)
    for encrypted_password in passwords:
        decrypted_password = decrypt_password(encrypted_password[0])
        passwords_display.insert(tk.END, decrypted_password + '\n')

# Connect to the database and create passwords table
conn, cursor = connect_to_database()
create_passwords_table(cursor)

# Create main window
app = tk.Tk()
app.title("Password Generator App")

# Tab control
tab_control = ttk.Notebook(app)
tab_generate = ttk.Frame(tab_control)
tab_database = ttk.Frame(tab_control)
tab_control.add(tab_generate, text='Generate Password')
tab_control.add(tab_database, text='Database')
tab_control.pack(expand=1, fill='both')

# --- Generate Password Tab ---

# Title box
title_label = tk.Label(tab_generate, text="Password Generator", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=3)

# Information text box
info_label = tk.Label(tab_generate, text="Configure password options and generate safe passwords.", wraplength=300, justify=tk.LEFT)
info_label.grid(row=1, column=0, columnspan=3)

# Checkboxes
special_char_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()

special_char_check = tk.Checkbutton(tab_generate, text="Special Characters", variable=special_char_var)
digit_check = tk.Checkbutton(tab_generate, text="Digits", variable=digit_var)
lowercase_check = tk.Checkbutton(tab_generate, text="Lowercase Characters", variable=lowercase_var)
uppercase_check = tk.Checkbutton(tab_generate, text="Uppercase Characters", variable=uppercase_var)

special_char_check.grid(row=2, column=0)
digit_check.grid(row=2, column=1)
lowercase_check.grid(row=3, column=0)
uppercase_check.grid(row=3, column=1)

# Length slider
length_label = tk.Label(tab_generate, text="Password Length:")
length_slider = tk.Scale(tab_generate, from_=6, to=20, orient=tk.HORIZONTAL)
length_label.grid(row=4, column=0, sticky=tk.E)
length_slider.grid(row=4, column=1)

# Generate Password button
generate_button = tk.Button(tab_generate, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=5, column=0, columnspan=2)

# Display generated password
password_display = tk.Text(tab_generate, height=1, width=30)
password_display.grid(row=6, column=0, columnspan=2)

# Save on Database button
save_button = tk.Button(tab_generate, text="Save on Database", command=save_password_gui)
save_button.grid(row=7, column=0, columnspan=2)

# Regenerate button
regenerate_button = tk.Button(tab_generate, text="Regenerate", command=generate_password_gui)
regenerate_button.grid(row=8, column=0, columnspan=2)

# --- Database Tab ---

# Passwords display
passwords_display = tk.Text(tab_database, height=10, width=40)
passwords_display.grid(row=0, column=0, padx=20, pady=20)

# Fetch Passwords button
fetch_button = tk.Button(tab_database, text="Fetch Passwords", command=fetch_passwords_gui)
fetch_button.grid(row=1, column=0, pady=10)

# Run the Tkinter main loop
app.mainloop()

# Close the database connection
conn.close()
