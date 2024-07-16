import random as rd
from time import sleep as sp
import os


characters = {
    1 : {
        "name" : "Rock",
        "move" : """
    _______
---'   ____)
    (_____)
    (_____)
    (____)
---.__(___)
"""
        },
    2 : {
        "name" : "Paper",
        "move" : """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    },
    3 : {
        "name" : "Scissors",
        "move" : """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    },
}


def single_player() -> None:
    print("Single Player Mode\n")
    for character in characters:
        print("({}) {}". format(character, characters[character]["name"]))
    player_one_choice = int(input("Choose your move: ").strip())
    bot_choice = rd.choice(range(1,4))
    
    os.system('cls')
    battle_printer(player_one_choice, bot_choice)
    sp(1)
    
    result = battle_result(player_one_choice, bot_choice)
    print("\n{}".format(result))

    if result == "You Win!":
        add_score()
    
    print("\n{}".format(score()))


def two_players() -> None:
    print("\n*Coming Soon...*")
    pass


def battle_printer(player_one = int, player_two = int) -> None:
    print("The Battle:")
    sp(.5)

    print("\n(Player One)\n\t{}{}".format(characters[player_one]["name"].upper(), characters[player_one]["move"]))
    sp(.5)

    print("\tVS.")
    sp(2)

    print("{}\n\t{}\n(Player Two)".format(characters[player_two]["move"], characters[player_two]["name"].upper()))


def battle_result(player_one = int, player_two = int) -> str:
    player_one
    player_two

    if player_one == player_two:
        return "Tie!"
    
    elif (player_one == 1 and player_two == 3) or (player_one == 2 and player_two == 1) or (player_one == 3 and player_two == 2):
        return "You Win!"
    
    else:
        return "You Lose!"
    

def add_score() -> None:
    previous_score = ""

    record = open("record.txt", "r")
    for char in record.read():
        if char in "1234567890":
            previous_score += char
    record.close()

    if previous_score in "1234567890":
        new_score = 1

    else:
        new_score = int(previous_score) + 1

    record = open("record.txt", "w")
    record.write("Score = {}".format(new_score))
    record.close()


def view_score():
    print(score)


def score() -> str:
    record = open("record.txt", "r")
    prompt = "" + record.read()
    record.close()

    return prompt