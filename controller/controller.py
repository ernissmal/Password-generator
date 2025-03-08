import time
from model.model import generate_password, generate_passphrase, generate_spell
from view.view import display_password, display_message


def validate_numeric_input(prompt, minimum=None, max_attempts=5):
    """Validate numeric input with optional minimum value and rate limiting."""
    attempts = 0
    while attempts < max_attempts:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                attempts += 1
                remaining = max_attempts - attempts
                print(f"Value must be at least {minimum}. {remaining} attempts remaining.")
                if attempts < max_attempts:
                    time.sleep(attempts * 0.5)  # Increasing delay with each attempt
                continue
            return value
        except ValueError:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Please enter a valid number. {remaining} attempts remaining.")
            if attempts < max_attempts:
                time.sleep(attempts * 0.5)  # Increasing delay with each attempt
    
    display_message("Too many invalid attempts. Please try again later.")
    exit(1)


def validate_yes_no_input(prompt, max_attempts=5):
    """Validate yes/no input with rate limiting."""
    attempts = 0
    while attempts < max_attempts:
        response = input(prompt).lower()
        if response in ["yes", "no"]:
            return response == "yes"
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Please enter 'yes' or 'no'. {remaining} attempts remaining.")
        if attempts < max_attempts:
            time.sleep(attempts * 0.5)  # Increasing delay with each attempt
    
    display_message("Too many invalid attempts. Please try again later.")
    exit(1)


def get_user_choice(max_attempts=5):
    """Prompt the user to choose the type of password to generate with rate limiting."""
    attempts = 0
    while attempts < max_attempts:
        print("Choose an option:")
        print("1. Generate a standard password")
        print("2. Generate a passphrase")
        print("3. Generate a spell-style password")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice in ['1', '2', '3']:
            return choice
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Invalid choice. Please select a valid option. {remaining} attempts remaining.")
            if attempts < max_attempts:
                time.sleep(attempts * 0.5)  # Increasing delay with each attempt
    
    display_message("Too many invalid attempts. Please try again later.")
    exit(1)
