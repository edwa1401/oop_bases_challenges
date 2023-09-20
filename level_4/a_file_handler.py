"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import csv
import json


class FileHandler:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read(self) -> str:
        with open(self.filename, 'r') as file:
            return file.read()


class JSONHandler(FileHandler):
    def read(self) -> dict[str, list[dict[str, str | list[str]]]]:
        with open(self.filename, 'r') as file:
            return json.load(file)


class CSVHandler(FileHandler):
    def read(self) -> list[dict[str, str]]:
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]


if __name__ == '__main__':
    reader_one = FileHandler(filename='data/text.txt')
    print(f'FileHandler: {reader_one.read()}')

    reader_two = JSONHandler(filename='data/recipes.json')
    print(f'JSONHandler: {reader_two.read()}')

    reader_three = CSVHandler(filename='data/user_info.csv')
    print(f'CSVHadler: {reader_three.read()}')