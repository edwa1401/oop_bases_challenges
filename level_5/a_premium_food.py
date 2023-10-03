"""
У нас есть базовый класс продукта, а так же есть миксин для продуктов питания, но нет класса для продуктов питания.

Задания:
    1. Нужно создать класс FoodProduct, который будет наследовать от классов Product и FoodProductMixin.
    2. У класса FoodProduct переопределить метод get_product_info, таким образом, чтобы если продукт премиальный, то в скобках
       в конце добавлялось слово Premium.
       Например: Product title: Avocado, price: 12 (Premium)'
    3. Создать экземпляр класс FoodProduct с ценой меньше 10 и вызвать у него метод get_product_info.
    3. Создать экземпляр класс FoodProduct с ценой больше 10 и вызвать у него метод get_product_info.
"""

from typing import Protocol

class ProductForm(Protocol):
    title: str
    price: float

    def get_product_info(self) -> str:
        ''' add metrhod'''


class Product:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def get_product_info(self) -> str:
        return f'Product title: {self.title}, price: {self.price}'


class FoodProductMixin:
    def is_premium_food(self: ProductForm) -> bool:
        return self.price > 10


class FoodProduct(FoodProductMixin, Product):
    def get_product_info(self) -> str:
        if self.is_premium_food():
            return f'Product title: {self.title}, price: {self.price} (Premium)'
        return super().get_product_info()

if __name__ == '__main__':
    tomat = FoodProduct(title='Pomidorka', price =9.01)
    apple = FoodProduct(title='Yablochko', price=10.50)

    print(tomat.get_product_info())
    print(apple.get_product_info())

