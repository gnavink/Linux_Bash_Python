from pathlib import Path
import csv

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73]
]

file_path = Path.home() / 'temperatures.csv'
with file_path.open(mode='w', encoding ='utf-8', newline ='') as file:
    writer = csv.writer(file)
    # for temp_list in daily_temperatures:
    #     writer.writerow(temp_list)
    writer.writerows(daily_temperatures) #Above 2 lines not requird


