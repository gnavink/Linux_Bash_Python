#List slicing
a = [1, 2, 3, 4, 5]
a[1] = 6               # a = [1, 6, 3, 4, 5]
a[2:4] = [10, 11]      # a = [1, 6, 10, 11, 5]
a[3:4] = [-1, -2, -3]  # a = [1, 6, 10, -1, -2, -3, 5]
a[2:] = [0]            # a = [1, 6, 0]

#Extended list striding. Number of elements in the right have to match the left side
a = [1, 2, 3, 4, 5]
a[1::2] = [10, 11]      # a = [1, 10, 3, 11, 5]
a[1::2] = [30, 40, 50]  # ValueError. Only two elements in slice on left

#List repetition
a = [3, 4, 5]
b = [a]
c = 4 * b  
a[0] = -7
print(c)            #[[-7, 4, 5], [-7, 4, 5], [-7, 4, 5], [-7, 4, 5]]

# If the variable c should not have references of its copies, then create a copy
# of each element
a = [ 3, 4, 5 ]
c = [list(a) for _ in range(4)]  # list() makes a copy of a list
