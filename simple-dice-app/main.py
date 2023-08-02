import tkinter as tk
from random import randint

# Functions
def roll() -> None:
    lbl_result['text'] = str(randint(1,6))

# Window
window = tk.Tk()
window.title('Dice App')
window.resizable(width=0, height=0)

# Widgets
frm_result = tk.Frame(window, relief='sunken', borderwidth=4)
lbl_result = tk.Label(frm_result, font=('Arial, 16'), width=17, pady=20)
frm_roll = tk.Frame(window, relief='flat', borderwidth=2)
btn_roll = tk.Button(frm_roll, text='Roll', font=('Arial, 12'), width=17, command=roll)

# Widgets Position
frm_result.grid(row=0, padx=4, pady=1, sticky='n')
lbl_result.grid(row=0, sticky='ns')
frm_roll.grid(row=1, padx=6, pady=3, sticky='ew')
btn_roll.pack() # Use .pack() when centering widgets... 

# Execute
window.mainloop()