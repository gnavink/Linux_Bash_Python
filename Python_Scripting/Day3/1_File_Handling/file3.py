from pathlib import Path

#Task 1: Do basic filehandling

str_path = '/home/navin/Documents/Professional/Training/DigiTerati/Python/Days_3_Python_Scripting_Training/data'
path = Path(str_path) 
path = path / 'hello.txt'

# #Type in Hello world in hello.txt
with path.open(mode='r', encoding='utf-8') as file:
    text = file.read()
print(text)

raise SystemExit()
#Task 2: Add multiple lines in the source file 'hello.txt'
# #Type in Hello world\nHelloWorld in hello.txt
with path.open(mode='r', encoding='utf-8') as file:
    text = file.read()
print(text)


#Task 3: Read line by line
# #Read a single line
with path.open(mode='r', encoding='utf-8') as file:
     for line in file.readlines():
         print(line)

with path.open(mode='r', encoding='utf-8') as file:
     for line in file.readlines():
         print(line,end='')


#Task4: Reading Non-Existing File
# #Create a non-existent file
#path = Path.home() / 'new_file.txt'
#with path.open(mode='r', encoding='utf-8') as file:
#    text = file.read()

#Task 5: Writing to a file
path = Path.cwd() / 'hello.txt'
with path.open(mode='w', encoding='utf-8') as file:
     file.write('Hi there!')

# #Check whats written
with path.open(mode='r', encoding='utf-8') as file:
    text = file.read()

print(text)


#Task 6:#Append mode
with path.open(mode='a', encoding='utf-8') as file:
    file.write('\nHello I am Navin here!!!')
    # file.seek(0)
    # file.read()

# raise SystemExit()

with path.open(mode='r', encoding='utf-8') as file:
    text = file.read()
print(text) 
