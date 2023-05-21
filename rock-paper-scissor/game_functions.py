import random as rd
from time import sleep as sp
import os

characters = {
    1 : {
        "name" : "Rock",
        "action" : """
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
        "action" : """
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
        "action" : """
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
    player_one_choice = int(input("Choose your action: ").strip())
    bot_choice = rd.choice(range(1,4))
    
    os.system('cls')
    battle_printer(player_one_choice, bot_choice)
    sp(.5)
    print("\n{}".format(winner(player_one_choice, bot_choice)))


def two_players() -> None:
    print("\n*Coming Soon...*")
    pass

def battle_printer(player_one = int, player_two = int) -> None:
    print("The Battle:")
    sp(.5)

    print("\n(Player One)\n\t{}{}".format(characters[player_one]["name"].upper(), characters[player_one]["action"]))
    sp(.5)

    print("\tVS.")
    sp(2)

    print("{}\n\t{}\n(Player Two)".format(characters[player_two]["action"], characters[player_two]["name"].upper()))



def winner(player_one = int, player_two = int) -> str:
    player_one
    player_two

    if player_one == player_two:
        return "Tie!"
    
    elif (player_one == 1 and player_two == 3) or (player_one == 2 and player_two == 1) or (player_one == 3 and player_two == 2):
        return "You Win!"
    
    else:
        return "You Lose!"