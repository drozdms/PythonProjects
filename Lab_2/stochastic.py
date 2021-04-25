from random import randint


class StochasticSet:

    def __init__(self):
        self.dict = {}
        self.list = list()

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict.update({val: len(self.list)})
        self.list.append(val)
        return True

    def remove(self, val):
        if val not in self.dict:
            return False
        buf = self.dict.pop(val)
        self.list[buf] = self.list[len(self.list) - 1]
        self.dict.update({self.list[buf]: buf})
        self.list.pop()
        return True

    def get(self):
        try:
            val = randint(0, len(self.list) - 1)
        except ValueError:
            return None
        return self.list[val]
