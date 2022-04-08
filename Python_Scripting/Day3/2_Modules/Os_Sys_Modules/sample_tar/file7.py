from pathlib import Path
import csv


file_path = Path.home() / 'temperatures.csv'
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


