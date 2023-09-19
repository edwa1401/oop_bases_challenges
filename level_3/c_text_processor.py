"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""

import re

class TextProcessor:
    def __init__(self, text: str) -> None:
        self.text = text

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summaryze(self) -> str:
        words = re.findall(r'\b\w+\b', self.text)
        return '{text_length} {num_words}'.format(
        text_length=super().summarize(),
        num_words=f', total number of words in the text: {len(words)}'
        )


if __name__ == '__main__':
    sentence_1 = 'one, two, three, fourth.'
    first_text = TextProcessor(text=sentence_1)
    print(first_text.to_upper())
    print(first_text.summarize())

    sentence_2 = 'five, six, seven.'
    second_text = AdvancedTextProcessor(text=sentence_2)
    print(second_text.to_upper())
    print(second_text.summaryze())


