import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length for your password: "))
        
        if length < 1:
            print("Password length should be at least 1.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return
    password = generate_password(length)
    print(f"Generated Password: {password}")
if __name__ == "__main__":
    main()
