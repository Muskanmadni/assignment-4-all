
import random

def guess_number():
    number = random.randint(1, 100)
    return number

def main():
    number = guess_number()
    print(number)

if __name__ == "__main__":
    main()