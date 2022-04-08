# def area(b, h):
#     return 0.5 * b * h

# area = lambda b, h: 0.5 * b * h
# print( area(6,5))

elements = [ (2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be") ]
elements.sort()
print(elements)

elements.sort(key=lambda e: (e[1], e[2]))
#elements.sort(key=lambda e: e[1:3])
print(elements)





