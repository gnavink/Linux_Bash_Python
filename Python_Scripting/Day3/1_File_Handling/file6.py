from pathlib import Path
import csv

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73]
]

str_path = '/home/navin/Documents/Professional/Training/DigiTerati/Python/Days_3_Python_Scripting_Training/data'
path = Path(str_path)
file_path = path / 'temperatures.csv'

# Remove the file before writing to see its effect
with file_path.open(mode='w', encoding ='utf-8', newline ='') as file:
    writer = csv.writer(file)
    # for temp_list in daily_temperatures:
    #     writer.writerow(temp_list)
    writer.writerows(daily_temperatures) #Above 2 lines not requird


