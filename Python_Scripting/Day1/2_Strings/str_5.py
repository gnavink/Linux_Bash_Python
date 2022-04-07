# str_5.py
#Demonstrates :
#               i)string methods eg. join, split. 
#              ii) Replication operator

#String Methods:

#lower()
s1 = 'Navin Kumar Gopalakrishnan'.lower()
print(s1)

#strip()
s1 = '  Navin Kumar GopalaKrishnan             '
print(s1.rstrip())
print(s1.lstrip())
print(s1.strip())

#   raise SystemExit()

#Startswith()
starship = 'Enterprise'
print (starship.startswith('en') )#False


#replace()
a = 'Hello World'
g = a.replace('Hello', 'Hello Cruel')  # f = 'Hello Cruel World'

#find()
print(g.find('ll', 0 , 9))
print(g.find('ll', 7 , 9)) # Not found = -1


# join()
s1 = ['India', 'fights', 'Corona']
s2 = ' '.join(s1)
print(s2)
print(type(s2)) 

# split()
s4 = 'Gandhiji*1869-10-02*1948-01-31'
fields = s4.split('*')
print(fields)


# * - replica 

s1 = '=' * 5 
print(s1)






# def split_fields(record) :
#     fields = record.split('*')
#     print(fields)
#     B_day = fields[1].split('-')
#     D_day = fields[2].split('-')
#     num_yrs_lived = int(D_day[0]) - int(B_day[0])
#     return num_yrs_lived

        
# num_yrs_lived = split_fields(s4)
# print(f'Gandhiji lived for {num_yrs_lived} years')


