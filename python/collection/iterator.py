from collections.abc import Iterator, Iterable
from typing import Any


class ConcreteIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection._container[self._position]
            self._position = self._position + 1
        except IndexError:
            raise StopIteration()

        return value


class ConcreteCollection(Iterable):
    def __init__(self):
        self._container = []

    def __iter__(self):
        return ConcreteIterator(self)

    def add_item(self, item: Any):
        self._container.append(item)


if __name__ == "__main__":
    collection = ConcreteCollection()
    collection.add_item('Hello')
    collection.add_item('Wolrd,')
    collection.add_item('Python.')

    for item in collection:
        print('{} '.format(item), end='')
    print('')
