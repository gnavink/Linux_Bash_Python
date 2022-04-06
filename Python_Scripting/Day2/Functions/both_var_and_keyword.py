def print_args(*args, **kwargs):
    for i, arg in enumerate(args):
        print(f'positional argument {i} {arg}') # f-string         
    for key in kwargs: #dict.keys() kwargs.keys()
        print(f'keyword argument {key} = {kwargs[key]}')
        

print_args(8,88, 100, one='no.1', two='no.2', three = 'no.3')