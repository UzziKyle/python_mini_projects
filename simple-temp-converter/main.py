'''
Lagyan ng ibang options next time
Madali lang naman 'yun
Add lang ng buttons to change units and conversions chuchu
'''
import tkinter as tk

# Variables
padding = 8
font = 'Arial, 12'

# Functions
def fahrenheit_to_celsius() -> None:
    fahrenheit = float(ent_temp_value.get())
    celsius = round(((fahrenheit - 32) * 5/9), 2)
    lbl_result['text'] = f'{celsius}\N{DEGREE CELSIUS}'

# Window
window = tk.Tk()
window.title('Temp Converter')
window.resizable(width=0, height=0)

# Widgets
frm_entry = tk.Frame(window)
ent_temp_value = tk.Entry(frm_entry, width=16)
ent_temp_value.insert(0, '0')
lbl_temp = tk.Label(frm_entry, text='\N{DEGREE FAHRENHEIT}', font=font)

btn_convert = tk.Button(window, text='\N{RIGHTWARDS BLACK ARROW}', font=font, command=fahrenheit_to_celsius)

lbl_result = tk.Label(window, text='-17.78\N{DEGREE CELSIUS}', font=font, width=8)

# Widgets Position
frm_entry.grid(row=0, column=0, padx=padding, pady=padding*1.5)
ent_temp_value.pack(side='left')
lbl_temp.pack(side='left')

btn_convert.grid(row=0, column=1, padx=padding)

lbl_result.grid(row=0, column=2, padx=padding)

# Execute
window.mainloop()