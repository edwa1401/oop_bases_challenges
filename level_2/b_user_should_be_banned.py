"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age
        self.status = 'not banned'

    def should_be_banned(self):
        if self.surname in SURNAMES_TO_BAN:
            self.status = 'banned'
        return self.status
    
if __name__ == '__main__':
    user_1 = User(name='Piter', surname='Pen', age=100)
    print(f'{user_1.name} {user_1.should_be_banned()}')
    banned_user = User(name='David', surname='Porter', age=50)
    print(f'{banned_user.name} {banned_user.should_be_banned()}')