"""
У нас есть класс Product, который содержит в себе информацию о продукте.
Еще у нас есть класс AlcoholProduct, но метод is_available для него не подходит, так как
алкоголь нельзя продавать с 5 утра до 11 вечера

Задания:
    1. Переопределите метод is_available в классе AlcoholProduct с использованием super()
    2. is_available у AlcoholProduct должен возвращать False если сейчас часы между 5 утра и 11 вечера.
       Для определения текущего часа можно использовать datetime.now().hour
    3. Создайте экземпляр класса AlcoholProduct и проверьте, можно ли сейчас продавать алкоголь.
"""
from datetime import datetime
import decimal

class Product:
    def __init__(self, title: str, price: decimal.Decimal, stock_quantity: decimal.Decimal) -> None:
        self.title = title
        self.price = price
        self.stock_quantity = stock_quantity

    def get_discounted_price(self, discount_percentage: decimal.Decimal) -> decimal.Decimal:
        return self.price * (1 - discount_percentage / 100)

    def is_available(self) -> bool:
        return self.stock_quantity > 0


class AlcoholProduct(Product):
    def is_available(self, current_hour: int) -> bool:
        if  current_hour < 5 and current_hour > 23:
            return False
        return super().is_available()

    
if __name__ == '__main__':
    cucumber = Product(title='огурцы', price=100.01, stock_quantity=1.050)
    print(cucumber.get_discounted_price(10))
    print('{title} в наличии? - {status}'.format(
        title=cucumber.title,
        status=cucumber.is_available())
        )

    vodka = AlcoholProduct(title='Столичная', price=1000.00, stock_quantity=10)
    print(vodka.get_discounted_price(5))
    print('{title} сейчас в наличии? - {status}'.format(
        title=vodka.title,
        status=vodka.is_available(current_hour=datetime.now().hour))
        )
    print('{title} сейчас в наличии? - {status}'.format(
        title=vodka.title,
        status=vodka.is_available(current_hour=6))
        )