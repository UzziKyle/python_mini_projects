# A mini program that draws a board
from os import system as sys

class Board:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def draw_self(self) -> None:
        rows = [x+1 for x in range(self.width)]

        for columns in rows:
            boxes = [x+1 for x in range(self.height)]

            for top in boxes:
                if top == boxes[-1]:
                    print(' ----')
                else:
                    print(' ----', end="")

            for side in boxes:
                if side == boxes[-1]:
                    print('|    ', end="|\n")
                else:
                    print('|    ', end="")

            if columns == rows[-1]:
                for bottom in boxes:
                    print(' ----', end="")

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

sys('cls') # Clears the screen

print("Hi! What board do you want me to draw?")
for num, board in enumerate(board_list):
    print("{}. {}".format(num+1, board["name"]))
num_input = int(input("Enter number: ").strip()) - 1

if num_input == len(board_list) - 1:
    input_width = int(input("Enter width: ").strip())
    input_height = int(input("Enter height: ").strip())
    custom = Board(input_width,input_height)

    board_list[num_input]["object"] = custom

# Final Output
board_list[num_input]["object"].draw_self()