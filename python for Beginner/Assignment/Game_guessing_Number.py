## Project 4: 
# 
# Game Guessing Number

import random

guess = []

cpu_num = random.randint(0,1000)

player_num = int(input("Enter a number between 0 to 1000 : "))

guess.append(player_num)

while player_num != cpu_num:
    if player_num > cpu_num:
        print("Too High !")
    else:
        print("Too Low !")
    player_num = int(input("Enter another number between 1 to 1000 : "))
    
    guess.append(player_num)
    
else:
    print("Well Done !!!")
    print("You have taken {} guesses ".format(len(guess)))
    print("Here are your guesses : ")
    print(guess)