import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Styling Variables
bgColor = '#F5EFE7'
txtColor = '#213555'
activeTxtColor = '#4F709C'
font = ('Arial', 12)

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Uzzi\'s Text Editor')
        self.iconbitmap('app-icon/app-icon.ico')
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=800, weight=1)
        self.minsize(800, 400)
        self.attributes('-fullscreen', False)

        # Widgets
        frm_buttons = tk.Frame(self, relief='raised', border=2, bg=bgColor)
        btn_open = tk.Button(frm_buttons, text='Open', font=font, fg=txtColor, activeforeground=activeTxtColor, command=lambda: self.open_file(txt_edit))
        btn_save = tk.Button(frm_buttons, text='Save As...', font=font, fg=txtColor, activeforeground=activeTxtColor, command=lambda: self.save_file(txt_edit))
        btn_fullscreen = tk.Button(frm_buttons, text='Toggle Fullscreen', font=font, fg=txtColor, activeforeground=activeTxtColor, command=lambda: self.toggle_fullscreen())
        txt_edit = tk.Text(self)
        txt_edit.insert(tk.END, '<!-- Write here -->')

        # Widgets Position
        frm_buttons.grid(row=0, column=0, sticky='ns')
        btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
        btn_save.grid(row=1, column=0, sticky='ew', padx=5)
        btn_fullscreen.grid(row=2, column=0, sticky='ew', padx=5, pady=35)
        txt_edit.grid(row=0, column=1, sticky='nsew')

    # Functions
    def open_file(self, txt_edit) -> None:
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )

        if not filepath: return
        
        txt_edit.delete('1.0', tk.END)
        with open(filepath, mode='r', encoding='utf-8') as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
            self.title(f'Uzzi\'s Text Editor - {filepath}')

    def save_file(self, txt_edit) -> None:
        filepath = asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
        )

        if not filepath: return

        with open(filepath, mode='w', encoding='utf-8') as output_file:
            text = txt_edit.get('1.0', tk.END)
            output_file.write(text)
        self.title('Uzzi\'s Text Editor - {filepath}')

    def toggle_fullscreen(self) -> None:
        '''
        self.attributes can be called with only a single argument to get the value of that argument.
        That's why walang nangyayari when I include a second argument, i.e. True
        Thank you, stackoverflow!
        '''
        if self.attributes('-fullscreen'):
            self.attributes('-fullscreen', False)
            return

        self.attributes('-fullscreen', True)

if __name__ == '__main__':
    app = App()
    app.mainloop()