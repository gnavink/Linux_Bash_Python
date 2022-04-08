# Compare two objects
def compare(a, b):
    if a is b:
        print('same object')
    if a == b:
        print('same value')
    if type(a) is type(b):
        print('same type')

>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> compare(a, a)
>>> compare(a, b)
>>> compare(a, [4,5,6])
