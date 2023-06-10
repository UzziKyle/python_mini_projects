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

board_funcs = ["Draw Box", "Matrix", "Quit"]

# Prints options and returns the chosen 
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

# Beginning of the program
print("BOARDS\nMain Menu:")
for num, item in enumerate(board_funcs):
    print("{}. {}".format(num+1,item))
menu_input = int(input("Enter number: ").strip())

sys('cls')

if menu_input == 1: # Draw Box
    print("Hi! What board do you want me to draw?")
    num_input = prompter()

    if num_input == len(board_list) - 1:
        custom_board(num_input)

    # Final Output
    board_list[num_input]["object"].draw_self()

elif menu_input == 2: # Matrix
    print("Hi! What matrix do you want?")
    num_input = prompter()

    if num_input == len(board_list) - 1:
        custom_board(num_input)

    # Final Output
    board_list[num_input]["object"].matrix()

elif menu_input == 3: # Quit
    print("Bye.") 
    quit()

else: 
    print("Stoopid!")
    quit()
