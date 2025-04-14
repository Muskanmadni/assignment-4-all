# hangman game user can guess the word

import random


def play_game():
    word = "apple , banana , cherry , date"

    word_list = word.split(",")
    random_word = random.choice(word_list)
    print("Guess the word: apple , banana , cherry , date")
    guess = input("Enter a letter: ")
    if guess in random_word:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")

play_game()