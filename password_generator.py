import random

def generate_password(length):
    """Generate a single password with the given length."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special_chars = "!@#$%^&*"

    # Start with an empty password
    password = ""

    # Add random lowercase letters to the password
    for _ in range(length - 2):  # Reserve space for one number and one uppercase letter
        password += random.choice(alphabet)

    # Add a random number
    password += random.choice(numbers)

    # Add a random uppercase letter
    password += random.choice(alphabet.upper())

    # Shuffle the characters in the password
    password = ''.join(random.sample(password, len(password)))

    return password

def main():
    """Main function to generate passwords."""
    print("Welcome to the Password Generator!")
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(num_passwords):
        try:
            length = int(input(f"Enter the length for password #{i + 1} (minimum 3): "))
            if length < 3:
                print("Password length must be at least 3. Setting length to 3.")
                length = 3
            password = generate_password(length)
            print(f"Password #{i + 1}: {password}")
        except ValueError:
            print("Invalid input. Skipping this password.")

    print("Thank you for using the Password Generator!")

if __name__ == "__main__":
    main()
