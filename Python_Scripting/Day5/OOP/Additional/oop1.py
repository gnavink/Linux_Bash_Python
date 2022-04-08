#oop1.py

#Illustrates: 
#        i) Creation of classes & Instances/objects
#       ii) Accessing Instance Data Attributes        

# class Employee():
#     pass

class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last  = last
        self.email = first + '.' + last + '@techm.com'
        self.pay  = pay
   
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


if __name__ == '__main__':

    # 1) Instance Creation Manually
    # emp_1 = Employee()
    # emp_2 = Employee()

    # print(emp_1)
    # print(emp_2)

    # emp_1.first = 'Navin'
    # emp_1.last = 'Kumar'
    # emp_2.first = 'Gnana'
    # emp_2.last = 'Prakash'

    # print(emp_1.first, emp_1.last)
    # print(emp_2.first, emp_2.last)

    # 2) Instance Creation Automatically
    emp_1 = Employee('Navin','Kumar',50000)
    emp_2 = Employee('Gnana','Prakash',80000)
  
    print(emp_1.email, emp_1.pay)
    print(emp_2.email, emp_2.pay)

    #3) Print Full name manually
    print(f'{emp_1.first} {emp_1.last}')  
    print(emp_1.fullname())

    #4) Classes & Instances way of invoking methods
    #print(emp_1.fullname())
    #print(Employee.fullname(emp_1))



     


