from main.model.user_group_base import users

# user_id_1 owes amount to user_id_2
from main.service.split_func import Split, SplitFactory


def add_p2p_expense(user_id_1: int, user_id_2: int, amount: float):
    add_expense(user_id_1, user_id_2, amount)


def add_expense(user_id_1: int, user_id_2: int, amount: float, group_id: int = 0):
    if user_id_1 in users and user_id_2 in users:
        users[user_id_1].update_balance_table(user_id=user_id_2, amount=amount, group_id=group_id)
        users[user_id_2].update_balance_table(user_id=user_id_1, amount=-amount, group_id=group_id)


def add_group_expense(group_id: int, base_user_id: int, user_list: list, split: str, amount: float):
    split_func = SplitFactory.get_split_func(split_func=split)
    split_obj = split_func(base_user_id=base_user_id, user_list=user_list, amount=amount)
    split_details = split_obj.run_split()
    for person in split_details:
        add_expense(person, base_user_id, split_details[person], group_id=group_id)


# user1 owes to user2 amount if amount is positive else user2 owes user 1
def settle_balance(user_id_1: int, user_id_2: int) -> float:
    balance_sheet = users[user_id_1].balance_table
    balance_sheet = balance_sheet[balance_sheet['user_id'] == user_id_2]
    net_amount = balance_sheet['amount'].sum()
    return net_amount
