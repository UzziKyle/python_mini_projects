import tkinter as tk

class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title('Counter App')
        self.resizable(False, False)

class MainFrame(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__()
        self.master = master
        self.relief = 'sunken'
        self.borderwidth = 5
        self.grid(row=0, sticky='nsew', padx=20, pady=20)

        # Widgets
        btn_decrease = tk.Button(self, text='-', font=('Arial, 12'), width=3, command=lambda: self.decrease_value(lbl_value))
        btn_increase = tk.Button(self, text='+', font=('Arial, 12'), width=3, command=lambda: self.increase_value(lbl_value))
        lbl_value = tk.Label(self, text='0', font=('Arial, 16'), width=3)

        # Widget Positions
        btn_decrease.grid(row=0, column=0, padx=15, ipadx=5, ipady=5)
        btn_increase.grid(row=0, column=2, padx=15, ipadx=5, ipady=5)
        lbl_value.grid(row=0, column=1, pady=10, sticky='ns')

    # Functions
    def increase_value(self, lbl_value) -> None:
        current_value = int(lbl_value['text'])
        if current_value == 999: return
        lbl_value['text'] = current_value + 1

    def decrease_value(self, lbl_value) -> None:
        current_value = int(lbl_value['text'])
        if current_value == 0: return
        lbl_value['text'] = current_value - 1

if __name__ == '__main__':
    window = Window()
    main_frame = MainFrame(window)
    window.mainloop()
