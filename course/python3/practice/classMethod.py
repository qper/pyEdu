task = """
Создайте класс BankAccount с атрибутами client_id, client_first_name, client_last_name, balance
и методами add() и withdraw(), при помощи которых можно пополнять счет и выводить средства со счета соответственно.
Атрибут balance должен инициализироваться по умолчанию значением 0.0 
и меняться при срабатывании методов add() и withdraw().
"""


class BankAccount:
    def __init__(self, client_id, client_first_name, client_last_name):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self. balance = 0.0

    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


account_1 = BankAccount(1, "Aleksei", "Smirnov")
account_2 = BankAccount(2, "Irina", "Smirnova")

print(account_1.client_id)
print(account_1.client_first_name)
print(account_1.client_last_name)
print(account_1.balance)

account_1.add(100)
print(account_1.balance)
account_1.withdraw(28.6)
print(account_1.balance)
account_1.add(50)
print(account_1.balance)
account_1.withdraw(5.85)
print(account_1.balance)
print(account_2.balance)