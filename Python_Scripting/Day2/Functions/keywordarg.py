import string

def letter_count(text, letters=string.ascii_letters):
    letters = set(letters)  
    #print(letters)
    count = 0
    for char in text:
        if char in letters:
            count += 1
    return count

string1= 'Navin and Nikhil'
count = letter_count(string1)
print(f'{count} length of input string: {len(string1)}') #Why printing 14 instead of 16 ??? 
print()
raise SystemExit() 

count = letter_count('Navin and Nikhil', 'aeiouAEIOU') # 2nd argument is positional
print(count)
print()



count = letter_count('Navin and Nikhil', letters = 'aeiouAEIOU') # 2nd argument is keyword
print(count)

