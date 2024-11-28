# model/model.py
import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True, use_uppercase=True, use_lowercase=True):
    """Generate a random password based on selected criteria."""
    
    # Character pools
    pool = ""
    if use_digits:
        pool += string.digits
    if use_special_chars:
        pool += string.punctuation
    if use_uppercase:
        pool += string.ascii_uppercase
    if use_lowercase:
        pool += string.ascii_lowercase

    # Generate the password
    password = ''.join(random.choice(pool) for _ in range(length))
    return password
