# password_generator.py

import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    symbols = string.punctuation if include_symbols else ''
    
    all_characters = lower + upper + digits + symbols
    if not all_characters:
        raise ValueError("At least one character set must be selected")
    
    return ''.join(random.choice(all_characters) for _ in range(length))

def generate_memorable_password(words_list, num_words=4):
    return '-'.join(random.choice(words_list) for _ in range(num_words))

def generate_hex_password(length=16):
    return ''.join(random.choice('0123456789abcdef') for _ in range(length))

def generate_base64_password(length=16):
    return ''.join(random.choice(string.ascii_letters + string.digits + '+/') for _ in range(length))

def generate_pronounceable_password(length=12):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    password = []
    for i in range(length):
        password.append(random.choice(consonants if i % 2 == 0 else vowels))
    return ''.join(password)

def generate_pin(length=4):
    return ''.join(random.choice(string.digits) for _ in range(length))

def generate_alphanumeric_password(length=12):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

if __name__ == '__main__':
    # Example usage
    print(generate_password())
    print(generate_memorable_password(['apple', 'banana', 'cherry', 'date', 'elderberry'], 3))
    print(generate_hex_password())
    print(generate_base64_password())
    print(generate_pronounceable_password())
    print(generate_pin())
    print(generate_alphanumeric_password())
