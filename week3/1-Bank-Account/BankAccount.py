class BankAccount:

    def __init__(self, name, balance, currency):
        self.history = []
        self.history.append("Account was created")
        self.name = name
        self.__balance = balance
        self.currency = currency

    def deposit(self, amount):
        self.history.append("Deposited {}{}".format(amount, self.currency))
        self.__balance += amount

    def balance(self):
        self.history.append('Balance check -> {}'.format(self.__balance))
        return self.__balance

    def withdraw(self, amount):
        return amount <= self.__balance

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.__balance, self.currency)

    def __int__(self):
        self.history.append("__int__ check -> {}".format(self.__balance))
        return self.__balance

    def transfer_to(self, account, amount):
        if not isinstance(account, BankAccount):
            raise TypeError("Account is not in type BankAccount")

        return account.currency == self.currency

    def history(self):
        return history
