import secrets
import string
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# App version
VERSION = "3.3"

# Path to the word list from .env
WORD_LIST_PATH = os.path.join(os.path.dirname(__file__), "..", os.getenv("DICTIONARY_PATH"))


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
