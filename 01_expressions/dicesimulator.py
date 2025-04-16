
import random

def roll_dice():
    return random.randint(1, 6)

def main():
    for i in range(3):
        roll1 = roll_dice()
        roll2 = roll_dice()
        print(f"Roll {i+1}: {roll1} and {roll2}")

if __name__ == "__main__":
    main()