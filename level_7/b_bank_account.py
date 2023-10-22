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

    def decrease_balance(self, amount: float) -> None:
        control_balance_amount = self.balance - amount
        if control_balance_amount < self.min_balance:
            raise ValueError('balance is less then -100')
        self.balance = control_balance_amount

if __name__ == '__main__':
    my_account = BankAccount(owner='me', balance=0.00)
    my_account.decrease_balance(50)
    print(my_account.balance)
    my_account.decrease_balance(50.01)


