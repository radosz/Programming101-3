class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {} bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def __add__(self, other):
        return self.amount + other.amount


class BillBatch:

    def __init__(self, list_b):
        self.list_b = list_b

    def __len__(self):
        return len(self.list_b)

    def __getitem__(self, index):
        return self.list_b[index]

    def total(self):
        return sum([int(x) for x in self.list_b])

    def __str__(self):
        return self.list_b


class CashDesk:

    money = []

    def __str__(self):
        return self.money

    def take_money(self, money):

        if isinstance(money, Bill):
            self.money.append(money)
        else:
            self.money = [m for m in money]

        return self.money

    def total(self):
        return sum(int(m) for m in self.money)

    def inspect(self):
        keys = [str(x) for x in self.money]
        values = [int(m) for m in self.money]
        return {k: v for k, v in zip(keys, values)}
