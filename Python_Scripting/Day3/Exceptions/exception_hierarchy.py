>>> d
{1: 'one', 2: 'two', 3: 'three'}
>>> d[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 5
>>> try:
...     x = d[5]
... except LookupError: 
...     print('Lookup Error Occurred')
... except KeyError:
...     print('Invalid key used')
... 
>>>Lookup Error Occurred