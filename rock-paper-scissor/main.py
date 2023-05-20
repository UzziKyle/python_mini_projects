import random as rd
from time import sleep as sp
import os
import game_functions as func

# A program that let's you play rock, paper, & scissors

game_modes = {
    1 : func.single_player,
    2 : func.two_players,
}

def init_game():
    os.system('cls') # Clears the terminal
    print("Welcome to Rock, Paper & Scissors!\n")
    game_mode_choice = int(input("Main Menu:\n(1) Single-player\n(2) Two-players\nEnter num of choice: ").strip())

    game_modes[game_mode_choice]()

    print("\n*The screen will be cleared after 5 seconds...*")
    sp(5)
    init_game()


init_game()