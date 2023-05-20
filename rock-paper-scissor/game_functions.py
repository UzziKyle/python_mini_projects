import random as rd

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
    print("\nSingle Player Mode\nOptions:")
    for character in characters:
        print("({}) {}". format(character, characters[character]["name"]))
    player_choice = int(input("Choose your action: ").strip())
    bot_choice = rd.choice(range(1,4))
    battle_printer(player_choice, bot_choice)

def two_players() -> None:
    print("\n*Coming Soon...*")
    pass

def battle_printer(player_one, player_two) -> None:
    print("\n{}{}\n\tVS.{}\n{}".format(characters[player_one]["name"], characters[player_one]["action"], characters[player_two]["action"], characters[player_two]["name"]))