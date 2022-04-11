import pandas as pd


class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.groups = []
        self.balance_table = pd.DataFrame(data=[], columns=['user_id', 'amount', 'group_id'])
        #
        # user-1
        # user_id amount group_id
        # 2       50      P2p
        # 2       -23    4
        #
        # user-2
        # 1    23   4
        # 1    -50  P2p

    def add_group(self, group_id: int):
        self.groups.append(group_id)

    def update_balance_table(self, user_id: int, amount: float, group_id: int):
        row = self.balance_table[self.balance_table.user_id == user_id]
        if row.empty:
            self.balance_table.append([user_id, amount, group_id])
        else:
            row['amount'] += amount
