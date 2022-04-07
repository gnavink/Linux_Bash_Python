# dict2.py

# Illustrates :
#        i) Creating a dict
#        ii) Nested dictionaries
#       iii) Updating a dict value
#        iv) Deleting a dict key

score = {}
print('Empty dictionary')
print(score)
print()

raise SystemExit()


print('Simple Dictionary')
score = {'Dhawan':84, 'Kohli':200}
print(score)
print()


print('Nested Dictionary')
score = { 'Test1':{'Dhawan':84, 'Kohli':200} , 
          'Test2':{'Dhawan':50}
        }
print(score)
print()

print('Update a Nested Dictionary')
score['Test1']['Dhawan'] = 0
print(score)
print()

print('Deleting a key in Dictionary')
del score['Test2']
print(score)
