"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса Employee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self):
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float) -> None:
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float) -> None:
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float) -> None:
        employee.salary -= amount


class Developer(ItDepartmentEmployee, SuperAdminMixin):
    def __init__(self, name: str, surname: str, age: int, salary: float, programming_language: str) -> None:
        super().__init__(name, surname, age, salary)
        self.programming_language = programming_language

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, programming language is {self.programming_language}'


if __name__ == '__main__':
    just_developer = Developer(
        name='Guido',
        surname='van Rossum',
        age=67,
        salary=1000000.01,
        programming_language='Python')
    
print(just_developer.get_info())

just_developer.increase_salary(just_developer, amount=1000000.00)

print(just_developer.get_info())

just_developer.decrease_salary(just_developer, amount=500000.00)

print(just_developer.get_info())




