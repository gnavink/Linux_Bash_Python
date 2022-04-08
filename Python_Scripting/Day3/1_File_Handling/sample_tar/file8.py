from pathlib import Path
import csv

file_path = Path.home() / 'employees_copy.csv'

def process_row(row):
    row['salary'] = float(row['salary'])
    return row


with file_path.open(mode='r', encoding ='utf-8', newline ='') as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
        print(row)
        #print(process_row(row))


