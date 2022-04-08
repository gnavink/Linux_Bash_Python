#oop3.py

#Illustrates :
# i)   Instance methods
# ii)  Class methods
# iii) Static Methods

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
        self.pay = self.pay * self.raise_amount

    @classmethod    
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


if __name__ == '__main__':

    emp_1 = Employee('Navin','Kumar',50000)
    emp_2 = Employee('Gnana','Prakash',80000)

    #1) Class methods used to set class variables
    # print(Employee.raise_amount)
    # Employee.set_raise_amount(1.05)
    # print(Employee.raise_amount)
    # print(emp_1.raise_amount)
    # print(emp_2.raise_amount)

    #2) Class methods as alternative constructor methods 

    # emp_str_1 = 'Praveen-Kumar-30000'

    # first, last, pay = emp_str_1.split('-')
    # new_emp_str_1  = Employee(first, last, pay)
    # #new_emp_str_1  =  Employee.from_string(emp_str_1)

    # print(new_emp_str_1.first)
    # print(new_emp_str_1.email)
    
    #3) Static methods
    # import datetime
    # my_day = datetime.date(2020, 5, 16)
    # print(Employee.is_workday(my_day))
    