'''
Nagtagal ako sa fullscreen option... paano ko ba ma-check 'yung attributes if fullscreen is True or not

Update: Check lines 43-45
'''
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Styling Variables
bgColor = '#F5EFE7'
txtColor = '#213555'
activeTxtColor = '#4F709C'
font = 'Arial, 12'

# Functions
def open_file() -> None:
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )

    if not filepath: return
    
    txt_edit.delete('1.0', tk.END)
    with open(filepath, mode='r', encoding='utf-8') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
        window.title(f'Uzzi\'s Text Editor - {filepath}')

def save_file() -> None:
    filepath = asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )

    if not filepath: return

    with open(filepath, mode='w', encoding='utf-8') as output_file:
        text = txt_edit.get(0, tk.END)
        output_file.write(text)
    window.title('Uzzi\'s Text Editor - {filepath}')

def toggle_fullscreen() -> None:
    '''
    window.attributes can be called with only a single argument to get the value of that argument.
    That's why walang nangyayari when I include a second argument, i.e. True
    Thank you, stackoverflow!
    '''
    if window.attributes('-fullscreen'):
        window.attributes('-fullscreen', False)
        return

    window.attributes('-fullscreen', True)

# Window
window = tk.Tk()
window.title('Uzzi\'s Text Editor')
window.iconbitmap('app-icon/app-icon.ico')
window.rowconfigure(0, minsize=600, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.minsize(800, 400)
window.attributes('-fullscreen', False)

# Widgets
frm_buttons = tk.Frame(window, relief='raised', border=2, bg=bgColor)
btn_open = tk.Button(frm_buttons, text='Open', font=font, fg=txtColor, activeforeground=activeTxtColor, command=open_file)
btn_save = tk.Button(frm_buttons, text='Save As...', font=font, fg=txtColor, activeforeground=activeTxtColor, command=save_file)
btn_fullscreen = tk.Button(frm_buttons, text='Toggle Fullscreen', font=font, fg=txtColor, activeforeground=activeTxtColor, command=toggle_fullscreen)
txt_edit = tk.Text(window)
txt_edit.insert(tk.END, '<!-- Write here -->')

# Widgets Position
frm_buttons.grid(row=0, column=0, sticky='ns')
btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)
btn_fullscreen.grid(row=2, column=0, sticky='ew', padx=5, pady=35)
txt_edit.grid(row=0, column=1, sticky='nsew')

# Execute
window.mainloop()