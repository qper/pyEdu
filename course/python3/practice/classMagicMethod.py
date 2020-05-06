task = """
Создайте класс Chain с атрибутом number_of_items.
Создайте два специальных метода в этом классе.

Первый должен при вызове встроенной функции print() для объекта этого класса выводить
'Chain with (значение number_of_items) items'

Второй должен при вызове встроенной функции len() для объекта этого класса
возвращать значение number_of_items этого объекта
"""


class Chain:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items

    def __str__(self):
        return f'Chain with {self.number_of_items} items'

    def __len__(self):
        return self.number_of_items


new_chain = Chain(55)

print(new_chain)
print(len(new_chain))
