#oop4.py

#Illustrates :
# i)   Inheritance


class Employee:

    raise_amount = 1.04
    num_employees = 0 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@scb.com'
        self.pay = pay

        self.__class__.num_employees += 1

    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount


# class Developer(Employee):
#     pass

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

if __name__ == '__main__':

    #1) Simple Inheritance without any methods in Developer class

    # dev_1 = Developer('Navin', 'Kumar', 50000)
    # dev_2 = Developer('Gnana', 'Prakash', 80000) 

    # print(dev_1.email)
    # print(dev_2.email)
    
    # print(help(Developer))

    #2) Set raise_amount to 10% developer class. See whether any change is present in Employee class
    # print(dev_1.pay)
    # dev_1.apply_raise()
    # print(dev_1.pay)

    #3) Developer Class has its own Constructor method
    dev_1 = Developer('Navin', 'Kumar', 50000, 'Python')
    dev_2 = Developer('Gnana', 'Prakash', 80000, 'C++')
    print(dev_1.email, dev_1.prog_lang)
    print(dev_2.email, dev_2.prog_lang)
