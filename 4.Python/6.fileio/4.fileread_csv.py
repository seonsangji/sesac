import csv

file_path = "test.csv"

data=[]

with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)

print(data)

