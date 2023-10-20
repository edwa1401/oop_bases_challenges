"""
У нас есть класс формы и метод для валидации в нем. Мы хотим создать форму для авторизации, где нам важно чтобы юзернэйм
существовал в базе данных

Задания:
    1. Напишите логику метода valid_form в классе AuthorizationFormMixin таким образом, чтобы там была проверка и из
       класса Form и проверка на то что юзернэйм есть в списке USERNAMES_IN_DB. Нужно использовать super() в этом методе
    2. Создайте класс AuthorizationForm, который будет наследником и от Form и от AuthorizationFormMixin
    3. Создайте экземпляр класса AuthorizationForm и вызовите у него метод valid_form. Должны отрабатывать обе проверки:
       и на длину пароля и на наличия юзернэйма в базе
"""
from typing import Protocol

USERNAMES_IN_DB = ['Alice_2023', 'BobTheBuilder', 'CrazyCoder', 'DataDiva', 'EpicGamer', 'JavaJunkie']

class HasUserName(Protocol):
    username: str

    def valid_form(self) -> bool:
        ''' add validation method'''


class Form:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def valid_form(self) -> bool:
        return len(self.password) > 8


class AuthorizationFormMixin:
    def valid_form(self: HasUserName) -> bool:
        return super().valid_form() and self.username in USERNAMES_IN_DB # type: ignore[misc]
    

class AuthorizationForm(AuthorizationFormMixin, Form):
    pass

if __name__ == '__main__':
    first_user = AuthorizationForm(username='Alice_2023', password='qwertyuio')
    second_user = AuthorizationForm(username='BobTheBuilder', password='abd')
    third_user = AuthorizationForm(username='user', password='123456789')

    print(first_user.valid_form())
    print(second_user.valid_form())
    print(third_user.valid_form())

    