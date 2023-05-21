import os
import game_functions as func

# A program that let's you play rock, paper, & scissors

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
        "name" : "Quit",
        "function" : exit,
    }
}

def init_game():
    os.system('cls') # Clears the terminal
    print("Welcome to Rock, Paper & Scissors!\n")
    main_menu()
    game_mode_choice = int(input("Enter num of choice: ").strip())

    os.system('cls')
    game_modes[game_mode_choice]["function"]()

    input("\nPress Enter to return to Main Menu...")
    init_game()

def main_menu():
    print("Main Menu")
    for item in game_modes.keys():
        print("({}) {}".format(item, game_modes[item]["name"]))
        
init_game()