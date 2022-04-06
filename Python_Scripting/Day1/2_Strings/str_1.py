#str_1.py

# Shows the usage of ' , ", """ quotes

a = "Single 'quotes' are fine; \"doubles\" must be escaped."
b = 'Single \'quotes\' must be escaped; "doubles" are fine.'

text = '''A triple quoted string like this can include 'quotes' and "quotes" without 
formality. We can also escape newlines 
so this particular string is actually only two lines long.'''

print(f'a = {a}')
print(f'b = {b}')
print(f'text = {text}')

print(f'Length of a is : {len(a)}')

paragraph = "This planet has—or rather had—a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."

print(f'paragraph = {paragraph}')






