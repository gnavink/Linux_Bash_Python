from pathlib import Path

lines_of_text = [
    'Hello from Line1\n',
    'Hello from Line2\n',
    'Hello from Line3\n'

]


#Task 1: Write multiple lines in an existent file
path = Path.cwd() / 'hello.txt'
with path.open(mode='w', encoding='utf-8') as file:
     file.writelines(lines_of_text)



#Task 2: Write multiple lines in a non-existent file
path = Path.cwd() / 'new_file.txt'
with path.open(mode='w', encoding='utf-8') as file:
    file.writelines(lines_of_text)



#Task 3: Write multiple lines in a non-existent file inside a non-existent folder
#Write a line to a file existing in a non-existent parent folder
path = Path.cwd() / 'new_folder' / 'new_file.txt'
#with path.open(mode='w', encoding='utf-8') as file:
#    file.write('Hello!!')



path.parent.mkdir(parents=True)
with path.open(mode='w', encoding='utf-8') as file:
    file.write('Hello!!')

raise SystemExit()



