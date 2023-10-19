"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс, но чтобы он не становился
       меньше чем значение в атрибуте класса min_balance. Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение
"""

EBAY_TITLE = 'eBay'


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def decrease_balance(self, amount: float):
        self.balance -= amount
        if self.balance < self.min_balance:
            self.balance += amount
            raise ValueError('balance is less then -100')
        return self.balance

        
if __name__ == '__main__':
    my_account = BankAccount(owner='me', balance=0.00)
    print(my_account.decrease_balance(50))
    print(my_account.decrease_balance(50.01))


