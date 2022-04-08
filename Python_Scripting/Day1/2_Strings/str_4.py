#str_4.py

# Illustrates :
#       i) Striding
#      ii) Slicing & Striding Together

s1 = 'he ate camel food'

#If start and end not given it defaults to: start=0 & end=len(string), stride index = 1 i not given
s2 = s1[::3]  
s3 = s1[::-2]

s4 = s1[:2:-2]
s5 = s1[-1:2:-2]

s6 = s1[0:-5:3]
s7 = s1[:-5:3]

print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's3 = {s3}')
print(f's4 = {s4}')
print(f's5 = {s5}')
print(f's6 = {s6}')
print(f's7 = {s7}')

#String Reverse
print(s1)
s1_reverse = s1[::-1]
print(f's1:{s1}, Reverse of s1:{s1_reverse}')

