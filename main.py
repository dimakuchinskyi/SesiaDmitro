class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Депозит {amount} грн. здійснено успішно.")
        else:
            print("Сума депозиту повинна бути більшою за 0.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount} грн. з рахунку.")
account = BankAccount("123456789", 1000)
print(f"Номер рахунку: {account.account_number}")
print(f"Поточний баланс: {account.balance} грн.")
account.deposit(500)
print(f"Поточний баланс: {account.balance} грн.")
account.withdraw(200)
print(f"Поточний баланс: {account.balance} грн.")
account.withdraw(1500)
