import random

number_to_guess = random.randint(1, 20)

while True:
    guess = int(input("Guess a number between 1 and 20: "))
    if guess < number_to_guess:
        print("Too low! You're as short as a hobbit!")
    elif guess > number_to_guess:
        print("Too high! You're as tall as a giraffe!")
    else:
        print("Congratulations! You're as smart as a wizard!")
        break