import secrets
import string
import os

# App version
VERSION = "3.3"

# Path to the word list
WORD_LIST_PATH = os.path.join(os.path.dirname(__file__), "../data/words.txt")


def load_word_list():
    """Load the word list from a file."""
    try:
        with open(WORD_LIST_PATH, "r") as file:
            words = [word.strip() for word in file.readlines()]
        if not words:
            raise ValueError("Word list is empty.")
        return words
    except FileNotFoundError:
        raise FileNotFoundError(f"Word list not found at {WORD_LIST_PATH}")


def generate_password(length=12, use_digits=True, use_special_chars=True, use_uppercase=True, use_lowercase=True):
    """Generate a random secure password."""
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

    if not pool:
        raise ValueError("At least one character set must be selected!")

    # Generate a password using secrets for better randomness
    password = ''.join(secrets.choice(pool) for _ in range(length))
    return password


def generate_passphrase(word_count=4, delimiter="-"):
    """Generate a secure passphrase using random words."""
    words = load_word_list()  # Load words dynamically
    passphrase = delimiter.join(secrets.choice(words) for _ in range(word_count))
    return passphrase


def generate_spell(length=12):
    """Generate a fantasy-style password."""
    prefixes = ["Drak", "Fyro", "Myst", "Shadow", "Arc"]
    suffixes = ["nix", "bane", "fyre", "storm", "fang"]
    special_chars = "!@#$%^&*"
    middle = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length - 8))
    return f"{secrets.choice(prefixes)}{middle}{secrets.choice(suffixes)}{secrets.choice(special_chars)}"
