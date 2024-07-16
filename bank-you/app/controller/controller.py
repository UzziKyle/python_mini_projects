import pickle


class Controller:
    def __init__(self, model, view) -> None:
        self.model = model
        self.view = view

    def create_new_savings_account(self, new_savings_account: object) -> None:
        savings_accounts_records = self._load_savings_accounts_records()
        pass

    def get_savings_account(self, account_number: int, pin_code: str):
        savings_accounts_records = self._load_savings_accounts_records()
        pass

    def delete_savings_account(self, account_number: int):
        savings_accounts_records = self._load_savings_accounts_records()
        pass

    def update_savings_account(self, account_number):
        savings_accounts_records = self._load_savings_accounts_records()
        pass

    def _load_savings_accounts_records(self):
        with open('savings_accounts_record.pkl', 'rb') as file:
            savings_accounts = pickle.load(file)

        return savings_accounts
