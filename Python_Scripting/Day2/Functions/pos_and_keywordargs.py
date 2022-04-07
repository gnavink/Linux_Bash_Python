def sum_of_powers(*args, power=1): # 1 ^ 2 + 3 ^ 2 + 5 ^ 2
    result = 0
    for arg in args:
        result += arg ** power
    return result

#retval = sum_of_powers(1, 3, 5) #Default positional argument for power 
retval = sum_of_powers(1, 3, 5, power = 2) # Use python shell to verify
print(retval)
