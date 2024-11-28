# main.py

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

def main():
    """Main function to handle password generation and display the result."""
    
    # Example: Generate a password with default options
    password = generate_password(length=12)

    # Output the generated password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
