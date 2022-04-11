from main.model.group import Group
from main.model.user import User
from main.model.user_group_base import users, groups


def add_user(user: User):
    users[user.user_id] = user


def remove_user(user_id: int):
    users.pop(user_id)


def add_group(group: Group):
    groups[group.group_id] = group


def remove_group(group_id: int):
    groups.pop(group_id)
