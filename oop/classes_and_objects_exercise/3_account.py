class Account:
    def __init__(self, id: int, name: str, balance=0):
        self.name = name
        self.id = id
        self.balance = balance

    def credit(self, amount) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount) -> [int, str]:
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self) -> str:
        name = self.name
        id = self.id
        balance = self.balance
        return f"User {name} with account {id} has {balance} balance"


account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())

