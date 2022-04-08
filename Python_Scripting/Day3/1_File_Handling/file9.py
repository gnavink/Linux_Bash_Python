from pathlib import Path
import csv

people = [
    {'name': 'Navin', 'age': 45},
    {'name': 'Pravin', 'age': 42}
]


str_path = '/home/navin/Documents/Professional/Training/DigiTerati/Python/Days_3_Python_Scripting_Training/data'
path = Path(str_path)
file_path = path / 'people.csv'

with file_path.open(mode='w', encoding ='utf-8', newline ='') as file:
    writer = csv.DictWriter(file, fieldnames = ['name','age'])
    writer.writeheader()
    writer.writerows(people)

