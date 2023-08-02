import tkinter as tk

# Functions
def increase_value() -> None:
    current_value = int(lbl_value['text'])
    if current_value == 999: return
    lbl_value['text'] = current_value + 1

def decrease_value() -> None:
    current_value = int(lbl_value['text'])
    if current_value == 0: return
    lbl_value['text'] = current_value - 1

# Window
window = tk.Tk()
window.title('Counter App')
window.resizable(width=0, height=0)

# Widgets
frm_main = tk.Frame(window, relief='sunken', borderwidth=5)
btn_decrease = tk.Button(frm_main, text='-', font=('Arial, 12'), width=3, command=decrease_value)
btn_increase = tk.Button(frm_main, text='+', font=('Arial, 12'), width=3, command=increase_value)
lbl_value = tk.Label(frm_main, text='0', font=('Arial, 16'), width=3)

frm_main.grid(row=0, sticky='nsew', padx=20, pady=20)
btn_decrease.grid(row=0, column=0, padx=15, ipadx=5, ipady=5)
btn_increase.grid(row=0, column=2, padx=15, ipadx=5, ipady=5)
lbl_value.grid(row=0, column=1, pady=15, sticky='ns')

# Execution
window.mainloop()
