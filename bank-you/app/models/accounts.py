import datetime


def validate_new_account_number(new_account_number: int) -> bool:
    return isinstance(new_account_number, int) and (new_account_number >= 0)


def validate_new_pin_code(new_pin_code: str, required_pin_length: int = 6) -> bool:
    pin_code_is_string: bool = isinstance(new_pin_code, str)

    if pin_code_is_string:
        length_is_valid: bool = len(new_pin_code) == required_pin_length
        characters_are_digit: bool = new_pin_code.isdigit()

        return length_is_valid and characters_are_digit

    return False


class BaseClass():
    def __init__(self) -> None:
        super().__init__()

        self._created_at: str = datetime.datetime.now()

    @property
    def created_at(self) -> str:
        return self._created_at


class SavingsAccount(BaseClass):
    def __init__(self, account_number: int, balance: float, pin_code: str) -> None:
        super().__init__()
        self._account_number: int = account_number
        self._balance: float = float(balance)
        self._pin_code: str = pin_code

    @property
    def account_number(self) -> int:
        return self._account_number

    @account_number.setter
    def account_number(self, new_account_number: int) -> None:
        try:
            is_valid_account_number = validate_new_account_number(
                new_account_number)

            if not is_valid_account_number:
                raise ValueError

            self._account_number = new_account_number

        except ValueError:
            print("Invalid account number.")

    @property
    def balance(self) -> float:
        return f'{self._balance:.2f}'

    @balance.setter
    def balance(self, new_balance) -> None:
        try:
            if new_balance < 0:
                raise ValueError

            self._balance = new_balance

        except ValueError:
            print("No negative balance.")

    @property
    def pin_code(self) -> str:
        return self._pin_code

    @pin_code.setter
    def pin_code(self, new_pin_code: str):
        try:
            is_valid_pin_code = validate_new_pin_code(new_pin_code)

            if not is_valid_pin_code:
                raise ValueError

            self._pin_code = new_pin_code

        except ValueError:
            print("Invalid pin code.")


if __name__ == "__main__":
    test = SavingsAccount(account_number=0, balance=100, pin_code="000000")
    print(test.account_number)
    print(test.balance)
    print(test.created_at)
