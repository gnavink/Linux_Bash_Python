import math

def area_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

#area = area_triangle(3,4,5)  
area = area_triangle(3,4)
print(area)
