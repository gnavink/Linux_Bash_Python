# pcost.py
#
# Reads input lines of the form 'NAME,SHARES,PRICE'.
# For example:
#
#    SYM,123,456.78

import sys
from pathlib import Path

if len(sys.argv) != 2:
    print(len(sys.argv))
    raise SystemExit(f'Usage: {sys.argv[0]} filename')

str_path = '/home/navin/Documents/Professional/Training/DigiTerati/Python/Days_3_Python_Scripting_Training/data'
path = Path(str_path)
filename = sys.argv[1]
file_path = path / filename
print(file_path)



# rows is a list of this form
# [
#   ['SYM', '123', '456.78']
#   ...
# ]


rows = []
with file_path.open(mode='r', encoding='utf-8') as file:
    for line in file:
        rows.append(line.split(','))


total = sum([int(row[1]) * float(row[2]) for row in rows ])
print(f'Total cost: {total:0.2f}')
