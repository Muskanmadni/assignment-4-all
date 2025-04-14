import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    """
    Generate a random password with specified characteristics.
    
    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_numbers (bool): Include numbers
        use_special (bool): Include special characters
    
    Returns:
        str: Generated password
    """
    # Define character sets
    uppercase = string.ascii_uppercase if use_uppercase else ''
    lowercase = string.ascii_lowercase if use_lowercase else ''
    numbers = string.digits if use_numbers else ''
    special = '!@#$%^&*()_+-=[]{}|;:,.<>?' if use_special else ''
    
    # Combine all allowed characters
    all_chars = uppercase + lowercase + numbers + special
    
    # Ensure at least one character from each selected set
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_lowercase:
        password.append(random.choice(lowercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special:
        password.append(random.choice(special))
    
    # Fill the rest of the password with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle the password to randomize the order
    random.shuffle(password)
    
    return ''.join(password)

def main():
    # Example usage
    print("Welcome to the Password Generator!")
    print("\nGenerating a 12-character password with all character types:")
    password = generate_password()
    print(f"Generated Password: {password}")
    
    print("\nGenerating a 16-character password with only letters and numbers:")
    password = generate_password(length=16, use_special=False)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()