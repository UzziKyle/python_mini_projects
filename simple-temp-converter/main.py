'''
Add other options next time
'''
import tkinter as tk

# Styling Variables
padding = 8
font = ('Helvetica', 12)

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Temp Converter')
        self.resizable(False, False)

        # Widgets
        frm_entry = tk.Frame(self)
        ent_temp_value = tk.Entry(frm_entry, width=16)
        ent_temp_value.insert(0, '0')
        lbl_temp = tk.Label(frm_entry, text='\N{DEGREE FAHRENHEIT}', font=font)
        btn_convert = tk.Button(self, text='\N{RIGHTWARDS BLACK ARROW}', font=font, command=lambda: fahrenheit_to_celsius())
        lbl_result = tk.Label(self, text='-17.78\N{DEGREE CELSIUS}', font=font, width=8)

        # Widgets Position
        frm_entry.grid(row=0, column=0, padx=padding, pady=padding*1.5)
        ent_temp_value.pack(side='left')
        lbl_temp.pack(side='left')
        btn_convert.grid(row=0, column=1, padx=padding)
        lbl_result.grid(row=0, column=2, padx=padding)

        # Functions
        def fahrenheit_to_celsius() -> None:
            fahrenheit = float(ent_temp_value.get())
            celsius = round(((fahrenheit - 32) * 5/9), 2)
            lbl_result['text'] = f'{celsius}\N{DEGREE CELSIUS}'

if __name__ == '__main__':
    app = App()
    app.mainloop()
