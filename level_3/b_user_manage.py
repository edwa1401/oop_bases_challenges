"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self) -> None:
        self.usernames: list[str] = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        try:
            self.usernames.remove(username)
        except ValueError:
            print('Такого пользователя не существует')
        

class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()


if __name__ == '__main__':
    users = UserManager()
    users.add_user(username='first_user')
    users.add_user(username='second_user')
    print(users.get_users())

    print('-----------------------------')
    beatles = AdminManager()
    beatles.add_user(username='John')
    beatles.add_user(username='Paul')
    beatles.add_user(username='George')
    beatles.add_user(username='Ringo')
    print(beatles.get_users())
    beatles.ban_username(username='John')
    print(beatles.get_users())
    beatles.ban_username(username='Gimmy')
    print('------------------------------')

    reservoir_dogs = SuperAdminManager()
    reservoir_dogs.add_user(username='mr White')
    reservoir_dogs.add_user(username='mr Pink')
    reservoir_dogs.add_user(username='mr Brown')
    reservoir_dogs.ban_username(username='mr Brown')
    print(reservoir_dogs.get_users())
    reservoir_dogs.ban_all_users()
    print(reservoir_dogs.get_users())

