# Password Generator Documentation

## Overview
This password generator application provides multiple ways to create secure passwords using a Model-View-Controller (MVC) architecture. The application offers three types of password generation:

1. Standard passwords - customizable with options for length and character types
2. Passphrases - word-based passwords with configurable delimiters
3. Spell-style passwords - specialized password format with minimum length requirements

## Architecture

### Controller (`controller.py`)
The controller manages user input and orchestrates the application flow:
- `get_user_choice()` - Prompts for password generation type
- `get_user_input()` - Collects parameters for standard password generation
- `get_passphrase_config()` - Collects parameters for passphrase generation
- `main()` - Core function that drives the application flow

### Model (`model.py`)
The model contains the password generation logic:
- `generate_password()` - Creates standard passwords with customizable options
- `generate_passphrase()` - Creates word-based passwords
- `generate_spell()` - Creates specialized "spell-style" passwords

### View (`view.py`)
The view handles displaying information to the user:
- `display_password()` - Shows the generated password
- `display_message()` - Shows custom messages

## Usage
Run the application and follow the prompts to choose a password type and configure its parameters. The application will guide you through the necessary inputs based on your selection and display the resulting password.

## Error Handling
The application includes basic error handling for invalid inputs, with recursive function calls to allow re-entry of information when errors occur.