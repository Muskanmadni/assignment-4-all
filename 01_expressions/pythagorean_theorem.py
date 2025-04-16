#Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math
def main():
    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = math.sqrt(a**2 + b**2)
    print(f"The length of the hypotenuse is {c:.2f}")

if __name__ == "__main__":
    main()


