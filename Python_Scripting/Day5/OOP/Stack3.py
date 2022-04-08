class Stack:
    def __init__(self, *, container=None):
        if container is None:
            container = list()
        self._items = container

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)




if __name__ == '__main__':
    import array
    s = Stack(container=array.array('i'))
    s.push(42)
    s.push(23)
    s.push('a lot')     # TypeError.