'''
Nalutang sa simula.
Antok na kasi ako.

Mag OOP sana ako pero nakalimutan ko paano simulan HAHA
Nag-tatry rin ako ng bago sa coding style ko.
Sakit pa rin sa mata.
Mas maganda pa rin ata 'yung code ko sa ACS form
'''

import tkinter as tk

# Styling Variables
paddingX = 10
paddingY = 5
marginX = 10
marginY = 10
backgroundColor = 'whitesmoke'
color = 'darkblue'
highlightColor = 'darkblue'

# Window
window = tk.Tk()
window.title('Address Entry Form')

# Widgets
# main container
frm_main = tk.Frame(
    master=window,
    bg=backgroundColor
)

frm_field_container = tk.Frame(
    master=frm_main,
    bg=backgroundColor,
    borderwidth=4,
    relief='sunken'
)

info_list = ['First Name', 'Last Name', 'Address Line 1', 'Address Line 2', 'City', 'State/Province', 'Postal Code', 'Country']
for index, info in enumerate(info_list):
    tk.Label(
        master=frm_field_container,
        bg=backgroundColor,
        fg=color,
        text=f'{info}:'
    ).grid(row=index, column=0, sticky='e')
    
    tk.Entry(
        master=frm_field_container, 
        width=50, 
    ).grid(row=index, column=1)

frm_btn_container = tk.Frame(
    master=frm_main,
    bg=backgroundColor
)

btn_clear = tk.Button(
    master=frm_btn_container,
    bg=backgroundColor,
    fg=color,
    width=8,
    text='Clear'
)

btn_submit = tk.Button(
    master=frm_btn_container,
    bg=backgroundColor,
    fg=color,
    width=8,
    text='Submit'
)
btn_clear.grid(row=0, column=0, sticky='e')
btn_submit.grid(row=0, column=1, sticky='e', padx=marginX)

# containers
frm_main.grid(row=1, sticky='nsew')
frm_field_container.grid(row=0, sticky='ew')
frm_btn_container.grid(row=1, sticky='e', pady=marginY)

# Execute Window
window.mainloop()
print('Application was closed.')