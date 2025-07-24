import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Character sets: letters, digits, symbols
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

main()