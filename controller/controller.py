from model.model import generate_password, generate_passphrase, generate_spell
from view.view import display_password, display_message


def get_user_choice():
    """Prompt the user to choose the type of password to generate."""
    while True:
        print("Choose an option:")
        print("1. Generate a standard password")
        print("2. Generate a passphrase")
        print("3. Generate a spell-style password")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid choice. Please select a valid option.")


def get_user_input():
    while True:
        # Get length with input validation
        while True:
            try:
                length = int(input("Enter password length: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        
        use_digits = input("Include digits? (yes/no): ").lower() == "yes"
        use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"

        if any([use_digits, use_special_chars, use_uppercase, use_lowercase]):
            return (length, use_digits, use_special_chars, use_uppercase, use_lowercase)
        else:
            print("You must select at least one character type (digits, special chars, uppercase, lowercase).")


def get_passphrase_config():
    """Get configuration for passphrase generation."""
    while True:
        try:
            word_count = int(input("Enter number of words for the passphrase: "))
            delimiter = input("Enter a delimiter for the passphrase (default is '-'): ").strip()
            if not delimiter:
                delimiter = "-"
            return word_count, delimiter
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to drive the application."""
    while True:
        # Get user's choice for the type of password
        choice = get_user_choice()

        if choice == '1':
            # Standard password generation
            length, use_digits, use_special_chars, use_uppercase, use_lowercase = get_user_input()
            password = generate_password(length, use_digits, use_special_chars, use_uppercase, use_lowercase)
            display_password(password)
            break

        elif choice == '2':
            # Passphrase generation
            word_count, delimiter = get_passphrase_config()
            passphrase = generate_passphrase(word_count, delimiter)
            display_message("Generated Passphrase:")
            display_password(passphrase)
            break

        elif choice == '3':
            # Spell-style password generation
            while True:
                try:
                    length = int(input("Enter the length of the spell (minimum 8): "))
                    if length >= 8:
                        spell = generate_spell(length)
                        display_message("Generated Spell:")
                        display_password(spell)
                        return
                    else:
                        print("Length must be at least 8 characters.")
                except ValueError:
                    print("Please enter a valid number.")
