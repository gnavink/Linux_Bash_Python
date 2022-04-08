# dict1.py

# () - Tuple ; tuple() 
# [] - list ; list()
# set()
# {} ; dict([])

#Illustrates :
#   i)  creating dict, 
#   ii) fetching dict keys & values

d0 = {}  
# d = { 'root': 18,  'blue': [75, 'R', 2],  21:'venus',
#        -14:None,  'mars': 'Rover',  (4,11): 18,  0:45 }
pairs = [('IBM', 125), ('ACME', 50), ('PHP', 40)]
d = dict(pairs)

print('Printing the dictionary')

print(d0)
print(d)
print('\n')

   
for key,item in d.items():
    print(key,  d[key] )
        
print('\n\n')

print('Print only the dictionary keys')
print(d.keys())

for i in d.keys(): # Iterating an iterable
    print(i)

print('Vallues of the keys')

# print('Print only the dictionary values')
# #print(d.values())
for i in d.values():
    print(i )

