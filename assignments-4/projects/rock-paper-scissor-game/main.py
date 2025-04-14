

import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    return user_choice  

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "Rock smashes scissors! You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "Paper covers rock! You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "Scissors cut paper! You win!"
    else:
        return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

play_game()