import os

#Task 1: Create with mkdir()
# os.mkdir('poems')
# print(os.path.exists('poems'))

#Task 2: Delete with rmdir()
# os.rmdir('poems')
# print(os.path.exists('poems'))

#Task 3: List Contents with listdir()
# os.mkdir('poems')
# print(os.listdir('poems'))
# os.mkdir('poems/mcintyre')
# print(os.listdir('poems'))

#Task 4: Create file inside mcintyre . 
fout = open('poems/mcintyre/the_good_man', 'wt')
fout.write('''Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
''')
fout.close()
print(os.listdir('poems/mcintyre'))

#Task 5: Change Current Directory with chdir()
os.chdir('poems')
print(os.listdir('.'))
print()
print()

#Task 6: List Matching Files with glob() . Run with Task 4 & 5

# * matches everything (re would expect .*)
# ? matches a single character
# [abc] matches character a, b, or c
# [!abc] matches any character except a, b, or c
import glob
print(glob.glob('m*'))
print(glob.glob('??')) #Any 2 letter file/directory
print(glob.glob('m??????e')) #eight-letter word that begins with m and ends with e
print(glob.glob('[klm]*e')) #begins with a k, l, or m, and ends with e


