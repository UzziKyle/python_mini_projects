# A mini program that either draws a board or return its matrix
from os import system as sys

class Board:
    def __init__(self, width=1, height=1) -> None:
        self.width = width
        self.height = height

    def draw_self(self) -> None:
        rows = range(self.height)
        columns = self.width

        for column in rows:
            print(" ----" * columns)
            print("|    " * columns, end="|\n")
        print(" ----" * columns)

    def matrix(self) -> None:
        rows = range(self.height)
        columns = range(self.width)
        matrix = []

        for row in rows:
            new_row = []
            for column in columns:
                new_row.append('')
            matrix.append(new_row)

        print(matrix)

domino = Board(12,12)
chess = Board(8,8)
tictactoe = Board(3,3)

board_list = [
    {
        "name": "Domino", 
        "object": domino,
        }, 
    {
        "name": "Chess", 
        "object": chess,
        }, 
    {
        "name": "TicTacToe", 
        "object": tictactoe,
        },
    {
        "name": "Custom",
    },
    ]

functions = ["Draw Box", "Matrix", "Quit"]

# prints options and returns the chosen 
def prompter() -> int:
    for num, board in enumerate(board_list):
        print("{}. {}".format(num+1, board["name"]))
    num_input = int(input("Enter number: ").strip()) - 1

    return num_input

# Creates a new custom board
def custom_board(list_index) -> None:
        input_width = int(input("Enter width: ").strip())
        input_height = int(input("Enter height: ").strip())
        custom = Board(input_width,input_height)

        board_list[list_index]["object"] = custom

sys('cls') # Clears the screen

print("BOARDS\nMain Menu:")
for num, item in enumerate(functions):
    print("{}. {}".format(num+1,item))
menu_input = int(input("Enter number: ").strip())

sys('cls')

# First two options
if menu_input == 1 or 2:
    print("Hi! What board?")
    num_input = prompter()

    if num_input == len(board_list) - 1:
        custom_board(num_input)

    if menu_input == 1:
        board_list[num_input]["object"].draw_self() # Draws Board

    else:
        board_list[num_input]["object"].matrix() # Returns Matrix

# Quit
elif menu_input == 3:
    print("Bye.") 
    quit()

else: 
    print("Stoopid!")
    quit()
