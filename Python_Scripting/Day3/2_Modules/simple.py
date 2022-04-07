#simple.py

x = 42

def spam(x):
    print(f'I am inside spam function')
    print(f'value of x is:{x}')

def run():
    print('Inside run')
    spam(x)

if __name__  == '__main__':   
    print('Running')
    run()
