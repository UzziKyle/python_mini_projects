# A program that let's you play rock, paper, & scissors
import os
import sys
import game_functions as func


game_modes = {
    1 : {
        "name" : "Single-player",
        "function" : func.single_player,
    },
    2 : {
        "name" : "Two-player",
        "function" : func.two_players,
    },
    3 : {
        "name" : "View Score",
        "function" : func.view_score,
    },
    4 : {
        "name" : "Quit",
        "function" : sys.exit,
    }
}


def main_menu():
    print("Main Menu")
    for item in game_modes.keys():
        print("({}) {}".format(item, game_modes[item]["name"]))


def init_game():
    os.system('cls') # Clears the terminal
    print("Welcome to Rock, Paper & Scissors!\n")
    main_menu()
    game_mode_choice = int(input("Enter num: ").strip())

    os.system('cls')
    game_modes[game_mode_choice]["function"]()

    input("\nPress Enter to return to Main Menu...")
    init_game()


init_game()
