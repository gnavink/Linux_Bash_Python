from pathlib import Path
import csv


str_path = '/home/navin/Documents/Professional/Training/DigiTerati/Python/Days_3_Python_Scripting_Training/data'
path = Path(str_path)
file_path = path / 'temperatures.csv'

#file_path = Path.home() / 'temperatures.csv'
daily_temperatures = []

with file_path.open(mode='r', encoding ='utf-8', newline ='') as file:
    reader = csv.reader(file)
    for row in reader:
        #Convert row to a list of integers
        int_row = [int(value)  for value in row]
        #Append the list of integers to daily_temperatures
        daily_temperatures.append(int_row)

print(daily_temperatures)
#print(dir(csv))


