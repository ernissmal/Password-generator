# controller/controller.py
from model.model import generate_password
from view.view import display_password

def get_user_input():
    """Get password configuration from the user."""
    length = int(input("Enter password length: "))
    use_digits = input("Include digits (yes/no)? ").lower() == 'yes'
    use_special_chars = input("Include special characters (yes/no)? ").lower() == 'yes' or 'y'
    use_uppercase = input("Include uppercase letters (yes/no)? ").lower() == 'yes' or 'y'
    use_lowercase = input("Include lowercase letters (yes/no)? ").lower() == 'yes' or "y"

    # Ensure that at least one character category is selected
    if not any([use_digits, use_special_chars, use_uppercase, use_lowercase]):
        print("You must select at least one character type (digits, special chars, uppercase, lowercase).")
        return get_user_input()  # Recursively ask for input again

    return length, use_digits, use_special_chars, use_uppercase, use_lowercase

def main():
    """Main function to drive the application."""
    # Get user input for password configuration
    length, use_digits, use_special_chars, use_uppercase, use_lowercase = get_user_input()

    # Generate the password using the model
    password = generate_password(length, use_digits, use_special_chars, use_uppercase, use_lowercase)

    # Display the password using the view
    display_password(password)
