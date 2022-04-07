L = [1,4, 10,  20]

def list_find(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == target:
            break
        index += 1
    else:
        index = -1
    return index


    

# def list_find(lst, target):  # Using for-loops
#     for index, x in enumerate(lst):
#         if x == target:
#             break
#     else:
#         index = -1
#     return index


#L = [1,2]
#>>> L.index(1)
#0
#>>> L.index(10)
# def list_find(lst, target):
#     index = -1    
#     index = lst.index(target)
#     return index

index = list_find(L, 100) #100
print(index)


