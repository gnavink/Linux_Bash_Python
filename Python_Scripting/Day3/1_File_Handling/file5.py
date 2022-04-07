# Demonstrate normal file writing

from pathlib import Path

temperature_readings = [68,65,68,70,74,72]

str_path = '/home/navin/Documents/Professional/Training/DigiTerati/Python/Days_3_Python_Scripting_Training/data'
path = Path(str_path)

file_path = path / 'temperatures.csv'
with file_path.open(mode='a', encoding = 'utf-8') as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:]:
        file.write(f',{temp}')

with file_path.open(mode='r', encoding='utf-8') as file:
    text = file.read()
print(text)
