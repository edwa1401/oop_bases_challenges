"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""
import decimal

class BankAccount:
    def __init__(self, owner_full_name: str, balance: decimal.Decimal) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: decimal.Decimal) -> None:
        self.balance += income
    
    def decrese_balance(self, expense: decimal.Decimal) -> None:
        self.balance -= expense
        if self.balance < 0:
            self.balance += expense
            raise ValueError(f'operation cancelled due to insufficient account balance {self.balance}')



if __name__ == '__main__':
    account = BankAccount(owner_full_name='Petr Petrovich Petrov', balance=100.01)
    account.decrese_balance(100)
    print(f'current balance {account.balance}')
    account.decrese_balance(1)
