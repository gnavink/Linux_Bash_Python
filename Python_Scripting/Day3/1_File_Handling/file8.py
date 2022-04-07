from pathlib import Path
import csv

str_path = '/home/navin/Documents/Professional/Training/DigiTerati/Python/Days_3_Python_Scripting_Training/data'
path = Path(str_path)
file_path = path / 'people.csv'

def process_row(row):
    row['salary'] = float(row['salary'])
    return row


with file_path.open(mode='r', encoding ='utf-8', newline ='') as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
        print(row)
        #print(process_row(row))


