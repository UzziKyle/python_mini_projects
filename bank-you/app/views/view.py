from os import system


def pagify(func):
    def wrapper():
        system("cls || clear")
        func()
    return wrapper


class View:
    def __init__(self) -> None:
        pass

    @staticmethod
    @pagify
    def show_no_records_found():
        print("No records found.")

    @staticmethod
    @pagify
    def show_auth_menu():
        print("1.) login    2.) create account  3.) exit")

    def show_actions_menu():
        print("1.) withdraw 2.) deposit 3.) check balance 4.) logout")
