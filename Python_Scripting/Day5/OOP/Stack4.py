#  Using Tuples
class Stack:
    def __init__(self):
        self._items = None
        self._size = 0

    def push(self, item):
        self._items = (item, self._items)
        self._size += 1

    def pop(self):
        (item, self._items) = self._items
        self._size -= 1
        return item
 
    def __repr__(self):
        return f'{type(self).__name__}[{self._items[:-1]}]'

    def __len__(self):
        return self._size

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()    # -> 3
    s.pop()    # -> 2
    print(dir(s))
    print(repr(s))