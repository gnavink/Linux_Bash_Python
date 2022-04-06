#list8.py

# Illustrates list Comprehension
# I wanted to have list with even numbers starting from 0 to 9
#List comprehension produces the list dynamically

list1 = [ i for i in range(10) if i % 2 == 0]

#Initialise a 4 x 3 matrix with zeros
#		  0 0 0 
#          0 0 0
#          0 0 0 
#          0 0 0
#          0 0 0 
list1 = [ [ 0  for i in range(3) ] for j in range(4)   ]

print(list1[0][0])
