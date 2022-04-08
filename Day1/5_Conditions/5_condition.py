## Sum of all even numbers

sum_of_evens = 0
for n in range(0,101,1): #range(101)
    if n % 2 == 0:
        sum_of_evens += n # sum_of_event = sum_of_event + n 
        print(n, end=' ')

print()
print(f'sum:{sum_of_evens}')
