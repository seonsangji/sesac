import csv

file_path = "test.csv"

data = [
    {"Name":"John", "Age": 25, "City": "Seoul"},
    {"Name":"Jane", "Age": 35, "City": "Busan"},
    {"Name":"Bob", "Age": 30, "City": "Jeju"},
]



for person in data:
    for key,value in person.items():
        print(f"Key:{key}, Value:{value}")    


with open(file_path, "w", newline="") as file:
    headers = ["Name","Age","City"]
    csv_writer = csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(data)
