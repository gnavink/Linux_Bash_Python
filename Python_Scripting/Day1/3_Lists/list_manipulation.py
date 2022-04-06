#list4.py
# Illustrates List manipulation using methods & indices
# i) extending the list
# ii) removing the list



list1 = [1, 3, 5,6]

# What should be done to add the elements 8,10,5 to list1? We have seen this before?
# What happens when we 'hello' is appended to list1
# list1.remove(5) #Removes the 1st occurence of element 5

list1 = [1, 3, 5, 6]
list2 = list1 

# What is list1 & list2 . Both should be same
list1[2:] = [7,8]
# What does list1 & list2 display now? Why?

list1 = [1, 3, 5, 6]
list1[2:] = [9, 10, 11]

#What does list1 display?

list1[0:2] = [7] 
#What does list1 display?