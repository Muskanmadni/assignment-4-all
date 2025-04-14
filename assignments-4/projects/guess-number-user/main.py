
import random


def main():
    
    number = random.randint(1, 10)
    user_guess = int(input("Enter your guess: "))
    if user_guess == number:
        print("You guessed the number!")
    else:
        print("You didn't guess the number!")

if __name__ == "__main__":
    main()