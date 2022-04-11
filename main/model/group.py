from main.errors.error import NoUserFoundInMemoryError
from main.model.user_group_base import users


class Group:
    def __init__(self, group_id: int, group_name: str):
        self.group_id = group_id
        self.group_name = group_name
        self.users = set()

    def add_user(self, user_id):
        if user_id in users:
            self.users.add(user_id)
        else:
            raise NoUserFoundInMemoryError(f'user id: {user_id} not in memory')

    def remove_user(self, user_id):
        self.users.remove(user_id)
