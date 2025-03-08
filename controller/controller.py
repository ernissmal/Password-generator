from model.model import generate_password, generate_passphrase, generate_spell
from view.view import display_password, display_message


def get_user_choice():
    """Prompt the user to choose the type of password to generate."""
    print("Choose an option:")
    print("1. Generate a standard password")
    print("2. Generate a passphrase")
    print("3. Generate a spell-style password")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice not in ['1', '2', '3']:
        print("Invalid choice. Please select a valid option.")
        return get_user_choice()  # Recursively ask for input again

    return choice


def get_user_input():
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

    if not any([use_digits, use_special_chars, use_uppercase, use_lowercase]):
        print("You must select at least one character type (digits, special chars, uppercase, lowercase).")
        return get_user_input()  # This is the only recursive call left
    
    return (length, use_digits, use_special_chars, use_uppercase, use_lowercase)


def get_passphrase_config():
    """Get configuration for passphrase generation."""
    try:
        word_count = int(input("Enter number of words for the passphrase: "))
    except ValueError:
        print("Please enter a valid number.")
        return get_passphrase_config()

    delimiter = input("Enter a delimiter for the passphrase (default is '-'): ").strip()
    if not delimiter:
        delimiter = "-"
    return word_count, delimiter


def main():
    """Main function to drive the application."""
    # Get user's choice for the type of password
    choice = get_user_choice()

    if choice == '1':
        # Standard password generation
        length, use_digits, use_special_chars, use_uppercase, use_lowercase = get_user_input()
        password = generate_password(length, use_digits, use_special_chars, use_uppercase, use_lowercase)
        display_password(password)

    elif choice == '2':
        # Passphrase generation
        word_count, delimiter = get_passphrase_config()
        passphrase = generate_passphrase(word_count, delimiter)
        display_message("Generated Passphrase:")
        display_password(passphrase)

    elif choice == '3':
        # Spell-style password generation
        try:
            length = int(input("Enter the length of the spell (minimum 8): "))
            if length < 8:
                print("Length must be at least 8 characters.")
                return main()  # Restart the process
        except ValueError:
            print("Please enter a valid number.")
            return main()

        spell = generate_spell(length)
        display_message("Generated Spell:")
        display_password(spell)
