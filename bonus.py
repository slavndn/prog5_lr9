from abc import abstractmethod


class BonusObserver:
    def __init__(self):
        self.users = {}
        self.bonus_levels = [
            {"level": "Silver", "min_spending": 0, "cashback": 0.01},
            {"level": "Gold", "min_spending": 2000, "cashback": 0.1},
            {"level": "Platinum", "min_spending": 5000, "cashback": 0.15},
        ]

    def determine_bonus_level(self, spending: int):
        if self.bonus_levels[2]["min_spending"] >= spending:
            return self.bonus_levels[2]["level"]
        elif self.bonus_levels[2]["min_spending"] >= spending:
            return self.bonus_levels[1]["level"]
        else:
            return self.bonus_levels[0]["level"]

    def update_user_spending(self, username, spending):
        self.users[username] = spending
        self._update_user_level(username)

    def _update_user_level(self, username):
        spending = self.users[username]
        current_level = self.determine_bonus_level(spending)
        self.users[username] = {"spending": spending,
                               "bonus_level": current_level}

    def get_user_bonus(self, username, password):
        return self.users.get(username)
