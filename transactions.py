class Transactions:
    def __init__(self, bonus_observer):
        self.bonus_observer = bonus_observer

    def add_transaction(self, username, password, amount):
        current_spending = self.bonus_observer.users.get(username, {}).get("spending", 0)
        new_spending = current_spending + amount
        self.bonus_observer.update_user_spending(username, new_spending)
