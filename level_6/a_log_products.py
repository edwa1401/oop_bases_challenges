"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знает о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""

from typing import Any


class PrintLoggerMixin:
    def log(self, message: Any) -> None:
        print (message)


class Product:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def get_info(self) -> str:
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(PrintLoggerMixin, Product):

    def increase_price(self) -> None:
        self.price *= 1.2
        super().log(self.price)

    def get_info(self) -> str:
        base_info = super().get_info()
        message = f'{base_info} (Premium)'
        super().log(message=message)
        return message

class DiscountedProduct(PrintLoggerMixin, Product):
    def increase_price(self) -> None:
        self.price /= 1.2
        super().log(self.price)

    def get_info(self) -> str:
        base_info = super().get_info()
        message = f'{base_info} (Discounted)'
        super().log(message=message)
        return message


if __name__ == '__main__':
    caviar = PremiumProduct(title='Икра черная осетровая', price=100000.01)
    zucchini = DiscountedProduct(title='Икра баклажанная заморская', price=1000.99)

    caviar.increase_price()
    caviar.get_info()

    zucchini.increase_price()
    zucchini.get_info()
