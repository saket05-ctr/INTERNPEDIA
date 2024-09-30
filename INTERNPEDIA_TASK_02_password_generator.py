import secrets
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Generate a secure random password based on specified criteria."""
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    
    character_pool = ""
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def get_user_input():
    """Get password generation preferences from the user."""
    try:
        length = int(input("Enter desired password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        return length, use_uppercase, use_lowercase, use_digits, use_symbols
    except ValueError:
        print("Invalid input. Please enter a valid number for length.")
        return get_user_input()

def generate_multiple_passwords():
    """Generate multiple passwords based on user input."""
    length, use_uppercase, use_lowercase, use_digits, use_symbols = get_user_input()
    num_passwords = int(input("How many passwords would you like to generate? "))

    passwords = [generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols) for _ in range(num_passwords)]
    
    print("\nGenerated Passwords:")
    for idx, password in enumerate(passwords):
        print(f"{idx + 1}: {password}")

    copy_to_clipboard = input("Would you like to copy the first password to clipboard? (y/n): ").lower() == 'y'
    if copy_to_clipboard:
        pyperclip.copy(passwords[0])
        print("First password copied to clipboard!")

if __name__ == "__main__":
    generate_multiple_passwords()
