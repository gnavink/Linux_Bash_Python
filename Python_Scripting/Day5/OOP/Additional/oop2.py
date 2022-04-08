#oop2.py

#Illustrates:
#          i) Class variables
#         ii) How are class variables accessed?


class Employee:

    raise_amount = 1.04
    num_employees = 0 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        self.__class__.num_employees += 1

    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay = self.pay * raise_amount
        self.pay = self.pay * self.raise_amount
        #self.pay = self.pay * self.__class__.raise_amount 



if __name__ == '__main__':

    print(Employee.num_employees)

    #1) Class variables
    emp_1 = Employee('Navin','Kumar',50000)
    emp_2 = Employee('Gnana','Prakash',80000)

    # emp_1.apply_raise()
    # print(emp_1.pay)
    # emp_2.apply_raise()
    # print(emp_2.pay)

    #2) Raise amount for an instance
    
    # emp_1.raise_amount = 1.05

    # print(emp_1.raise_amount)
    # print(Employee.raise_amount)
    # print(emp_2.raise_amount)
    # print()

    # print(emp_1.__dict__)
    # print()
    # print(emp_1.__class__.__dict__)
    
    #3) Specific use case of only class variables
    print(Employee.num_employees)