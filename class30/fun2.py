import random

while True:
    user_move = input("Enter rock, paper, or scissors: ")
    computer_move = random.choice(["rock", "paper", "scissors"])

    if user_move == computer_move:
        print("It's a tie! You're as boring as a lecture on crop rotation!")
    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "scissors" and computer_move == "paper") or \
         (user_move == "paper" and computer_move == "rock"):
        print("You win! You're as sneaky as a ninja!")
    else:
        print("You lose! You're as clumsy as a drunken pirate!")

