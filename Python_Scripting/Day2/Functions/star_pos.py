import math

def area_triangle(a, b, c, *, units="square meters"):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return f'{area} {units}'
    

#retval = area_triangle(25, 24, 7)  # returns: '84.0 square meters'
#retval = area_triangle(41, 9, 40, units="sq. inches") # returns: '180.0 sq. inches'
retval =  area_triangle(25, 24, 7, "sq. inches")  # WRONG! raises TypeError
retval =  area_triangle(25, 24, 7, 65)  # WRONG! raises TypeError

print(retval)

