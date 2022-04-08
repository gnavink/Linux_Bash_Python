import csv

#Task 1: Read from csv file
with open('routerlist.csv') as fh:
    data = list(csv.reader(fh))
    
print(data)

#Task 2: Read iteratively from csv file and process each line separately

with open('routerlist.csv') as fh:
    data = csv.reader(fh)

    for row in data:
        name = row[0]
        ip   = row[1]
        location = row[2]
        print(f"The router '{name}' with IP address '{ip}' is in the location '{location}'")

#Task 3: Write data to the file
hostname = input('Enter hostname: ')
ip       = input('Enter IP address: ')
location = input('Enter location: ')
router = [hostname , ip, location]

with open('routerlist.csv','a') as fh:
    csv_writer = csv.writer(fh, quoting = csv.QUOTE_ALL)
    csv_writer.writerow(router)





