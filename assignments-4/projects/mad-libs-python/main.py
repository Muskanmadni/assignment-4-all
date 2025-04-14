# Mad-libs-python project CLI
import random

def mad_libs():
    print("Welcome to Mad-Libs!")
    print("Please enter the following words:")

    # Get the user's name
    name = input("What is your name? ")

    # Get the user's age
    age = input("How old are you? ")

    # Get the user's favorite color
    favorite_color = input("What is your favorite color? ")

    # Get the user's favorite animal
    favorite_animal = input("What is your favorite animal? ")

    # Get the user's favorite food
    favorite_food = input("What is your favorite food? ")

    # Get the user's favorite Artist
    favorite_artist = input("What is your favorite artist? ")

    # Get the user's why they like the artist
    why_like_artist = input("Why do you like the artist? ")

    print(f"Hello {name}! You are {age} years old and your favorite color is {favorite_color}.")
    print(f"Your favorite animal is {favorite_animal} and your favorite food is {favorite_food}.")
    print(f"You like {favorite_artist} and {why_like_artist}.") 

    print("Thank you for playing Mad-Libs!")

if __name__ == "__main__":
    mad_libs()








