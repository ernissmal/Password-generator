import random
import string

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

# Validate password length
valid_length = False
while not valid_length:
    try:
        length = int(input("Enter the desired password length: "))
        if length > 0:
            valid_length = True
        else:
            print("Password length must be greater than zero.")
    except ValueError:
        print("Invalid input, please enter a valid number.")

# Validate character types selection
valid_chars = False
while not valid_chars:
    use_special_chars = get_confirmation("Use special characters? Y/N ")
    use_digits = get_confirmation("Use digits? Y/N ")
    use_lowercase_chars = get_confirmation("Use lowercase characters? Y/N ")
    use_uppercase_chars = get_confirmation("Use uppercase characters? Y/N ")
    
    if any([use_lowercase_chars, use_uppercase_chars, use_special_chars, use_digits]):
        valid_chars = True
    else:
        print("You must select at least one character type to generate a secure password!")

# Generate and print the password
password = generate_password(length, use_special_chars, use_digits, use_lowercase_chars, use_uppercase_chars)
print(f"Generated password: {password}")
