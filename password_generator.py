import random
import string
import os

class PasswordGenerator:
    def __init__(self):
        self.min_length = 12
        self.max_length = 20
        self.words_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/words_filtered.txt')
        
        # If the filtered words file doesn't exist yet, use the original words file
        if not os.path.exists(self.words_file):
            self.words_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/words.txt')
        
        self.load_words()

    def load_words(self):
        """Load words from dictionary file"""
        with open(self.words_file, 'r') as f:
            self.words = [word.strip() for word in f.readlines()]

    def generate(self, length=None):
        """Generate a random password with mixed characters"""
        if length is None:
            length = random.randint(self.min_length, self.max_length)
        
        # Ensure we have all required character types
        lowercase = random.choice(string.ascii_lowercase)
        uppercase = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)  # Add at least one digit
        special = random.choice(string.punctuation)
        
        # Generate the remaining characters
        remaining_length = length - 4  # 4 characters are already chosen
        remaining = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation, 
            k=remaining_length
        ))
        
        # Combine all parts and shuffle
        all_chars = lowercase + uppercase + digit + special + remaining
        password_chars = list(all_chars)
        random.shuffle(password_chars)
        
        return ''.join(password_chars)

    def generate_passphrase(self, word_count=4, separator='-'):
        """Generate a passphrase from random dictionary words"""
        selected_words = random.sample(self.words, word_count)
        return separator.join(selected_words)

    def generate_pin(self, length=4):
        """Generate a numeric PIN"""
        return ''.join(random.choice(string.digits) for _ in range(length))
