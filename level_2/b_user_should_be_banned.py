"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def should_be_banned(self) -> str:
        if self.surname in SURNAMES_TO_BAN:
            return f'user {self.name} is banned'
        else:
            return f'user {self.name} is not banned'
    
if __name__ == '__main__':
    not_banned_user = User(name='Piter', surname='Pen', age=100)
    print(not_banned_user.should_be_banned())

    banned_user = User(name='David', surname='Porter', age=50)
    print(banned_user.should_be_banned())