import tkinter as tk

# Functions
def increase_value() -> None:
    current_value = lbl_value['text']
    lbl_value['text'] = int(current_value) + 1

def decrease_value() -> None:
    current_value = lbl_value['text']
    lbl_value['text'] = int(current_value) - 1

# Window
window = tk.Tk()
window.title('Counter App')

# Widgets
frm_main = tk.Frame(window, relief='sunken', borderwidth=5)
btn_decrease = tk.Button(frm_main, text='-', font=('Arial, 12'), width=3, command=decrease_value)
btn_increase = tk.Button(frm_main, text='+', font=('Arial, 12'), width=3, command=increase_value)
lbl_value = tk.Label(frm_main, text='0', font=('Arial, 16'), width=3)

frm_main.grid(row=0, sticky='nsew')
btn_decrease.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5)
btn_increase.grid(row=0, column=2, padx=5, pady=5, ipadx=5, ipady=5)
lbl_value.grid(row=0, column=1, padx=10, pady=10, ipadx=5, ipady=5, sticky='ns')

# Execution
window.mainloop()