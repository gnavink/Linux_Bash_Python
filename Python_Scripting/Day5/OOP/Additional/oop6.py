#oop6.py
#Illustrates:
#      i) Dunder Methods: __repr__, __str__
#     ii) __add__, __len__

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f'Employee({self.first},{self.last},{self.pay})'
    
    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

if __name__ == '__main__':

    emp_1 = Employee('Navin','Kumar',50000)
    
    #1) repr, str
    # print(emp_1)
    # print(str(emp_1))
    # print(repr(emp_1))

    #2) Add two employee instances
    #emp_2 = Employee('Gnana','Prakash',80000)
    #print(emp_1 + emp_2)
    
    #3) __len__
    print(emp_1.fullname(),   len(emp_1))
    
    