def product(*args): #varible number of arguments
    result = 1
    for arg in args:
        result *= arg
    return result

#retval = product(1, 2, 3, 4) # args == (1, 2, 3, 4); returns: 24
#retval = product(5, 3, 8) # args == (5, 3, 8); returns: 120
retval = product(11) # args == (11,); returns: 11
#retval = product()
print(retval)




