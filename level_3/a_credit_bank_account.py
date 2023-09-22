"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':
    akakiy_bank_acc = BankAccount(owner_full_name='Akakiy Akakievich Akakiev', balance=1000.00)
    akakiy_bank_acc.increase_balance(100)
    akakiy_bank_acc.decrease_balance(50)
    print('{name} - {balance}'.format(
        name=akakiy_bank_acc.owner_full_name,
        balance=akakiy_bank_acc.balance
        ))

    marfa_cred_acc = CreditAccount(owner_full_name='Marfa Ivanova', balance=900.00)

    marfa_cred_acc.increase_balance(100.01)
    print('If {name} account eligible for credit? - {status}'.format(
        name=marfa_cred_acc.owner_full_name,
        status=marfa_cred_acc.is_eligible_for_credit()
        ))
    
    marfa_cred_acc.decrease_balance(1.00)
    print('And if {name} account is eligible for credit now? - {status}'.format(
    name=marfa_cred_acc.owner_full_name,
    status=marfa_cred_acc.is_eligible_for_credit()
    ))
