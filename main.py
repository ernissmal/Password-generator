import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = length_entry.get()
    if not length.isdigit():
        messagebox.showerror("Error", "Password length should be a positive integer.")
        return

    length = int(length)
    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.configure(bg="white")  # Set white background color

# Create a label and entry for password length
length_label = tk.Label(window, text="Password Length:", bg="white")  # Set white background color
length_label.pack()
length_entry = tk.Entry(window, bg="white")  # Set white background color
length_entry.pack()

# Create a button to generate password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label and entry to display the generated password
password_label = tk.Label(window, text="Generated Password:", bg="white")  # Set white background color
password_label.pack()
password_entry = tk.Entry(window, bg="white")  # Set white background color
password_entry.pack()

# Start the main event loop
window.mainloop()
