import array


class Transaction:

    def __init__(self, amount, name):
        self.__amount = 0
        self.__name = ""


class MaxPq:
    def __init__(self, size: int):
        self.pq = array()

