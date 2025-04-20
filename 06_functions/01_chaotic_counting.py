

import random

DONE_LIKELIHOOD = 0.2  # 20% chance of stopping at each number

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i, end=" ")

def main():
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()







