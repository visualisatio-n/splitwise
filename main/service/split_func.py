from abc import abstractmethod, ABC


class Split:
    def __init__(self, base_user_id: int, user_list: list, amount: float, shares_list: dict = None):
        self.base_user_id = base_user_id
        self.user_list = user_list
        self.amount = amount

    @abstractmethod
    def run_split(self) -> dict():
        pass


class EqualSplit(Split, ABC):
    def __init__(self, base_user_id: int, user_list: list, amount: float):
        super().__init__(base_user_id=base_user_id, user_list=user_list, amount=amount)

    def run_split(self) -> dict():
        per_person_share = self.amount / len(self.user_list)
        split_details = dict()
        if self.base_user_id in self.user_list:
            self.user_list.remove(self.base_user_id)
        for user_id in self.user_list:
            split_details[user_id] = per_person_share
        return split_details


class SplitFactory:
    @classmethod
    def get_split_func(cls, split_func: str):
        if split_func == 'equal':
            return EqualSplit
