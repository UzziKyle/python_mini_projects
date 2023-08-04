import tkinter as tk
from random import randint

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Dice App')
        self.resizable(width=0, height=0)

        # Widgets
        frm_result = tk.Frame(self, relief='sunken', borderwidth=4)
        lbl_result = tk.Label(frm_result, font=('Arial, 16'), width=15, pady=20)
        frm_roll = tk.Frame(self, relief='flat', borderwidth=2)
        btn_roll = tk.Button(frm_roll, text='Roll', font=('Arial, 12'), width=10, command=lambda: self.roll(lbl_result))

        # Widgets Position
        frm_result.grid(row=0, padx=5, pady=1, sticky='n')
        lbl_result.grid(row=0, sticky='ns')
        frm_roll.grid(row=1, padx=5, pady=3, sticky='ew')
        btn_roll.pack() # Use .pack() when centering widgets... 

    # Functions
    def roll(self, lbl_result) -> None:
        lbl_result['text'] = str(randint(1,6))

if __name__ == "__main__":
    app = App()
    app.mainloop()
