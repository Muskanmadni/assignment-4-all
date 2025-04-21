
import random

def main():
    secret_number = random.randint(1,10)
    print("Guess a number between 1 and 10")
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("You guessed the number!")
    else:
        print("Try again!")

if __name__ == "__main__":
    main()