# A program that generates a random password for you // first time using GUI

import PySimpleGUI as sg
import random as rd
from os import system as sys

def password_generator(size = 8, chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?")   -> str:
    password = rd.sample(chars,size)
    return"".join(password)

password_generator()

sg.theme('BlueMono')

layout = [  [sg.Text('Enter desires password length'), sg.InputText()],
            [sg.Button('Print'), sg.Button('Exit')] ]

window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    sys('cls')
    print(password_generator(int(values[0])))

window.close()