#oop5.py

#Illustrates :
# i)   Inheritance with Manager Class
# ii) Add/Remove/Print Employee methods
# iii) isinstance, issubclass methods


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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        self.employees = [] if employees is None else employees
        #if employees is None:
        #    self.employees = []
        #else:
        #    self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

if __name__ == '__main__':

    #3) Developer Class has its own Constructor method
    dev_1 = Developer('Navin', 'Kumar', 50000, 'Python')
    dev_2 = Developer('Gnana', 'Prakash', 80000, 'C++')
    print(dev_1.email, dev_1.prog_lang)
    print(dev_2.email, dev_2.prog_lang)

    #4) Add Manager Class

    mgr_1 = Manager('Raghu','Ram',100000,[dev_1])
    #print(mgr_1.email)
    #mgr_1.print_emps()

    # mgr_1.add_emp(dev_2)
    # mgr_1.print_emps()
    # print()

    # mgr_1.remove_emp(dev_1)
    # mgr_1.print_emps()

    #5) IsInstance , Issubclass 
    print(isinstance(mgr_1, Manager))
    #print(isinstance(mgr_1, Employee))
    #print(isinstance(mgr_1, Developer))
    #print(issubclass(Manager, Employee))