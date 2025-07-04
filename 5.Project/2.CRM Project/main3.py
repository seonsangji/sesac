import csv
from userdisplay import generateCSV
from storedisplay import generateCSV
from storedisplay import generateCSV

cls_path = [ userdisplay, storedisplay, itemdisplay]
csv_path = ["users.csv","stores.csv","items.csv"]
header = [
    ["Id", "Name", "Gender", "Birthdate", "Age", "Address"],
    ["Id", "Name", "Type", "Address"],
    ["Id", "Name", "Type", "Price"]
    ]

class GenerateMain:

    def __init__(self, csv_path, header):
        self.csv_path = csv_path
        self.header = header

    def generateInput1(self):
        dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item):").lower()
        self.dataType = dataType

    def writeCSV(self,data):
        with open (csv_path, "w", newline="", encoding="utf-8") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(header)
                csv_writer.writerows(data)

    def generateInput2(self, csv_path, header):
        getData = int(input("생성할 데이터 개수를 입력하세요 (숫자로):"))
        getForm = input("아웃풋 형태를 입력하세요 (csv, console):").lower()

        if getForm == 'csv':            
            data = generateCSV(getData)
            writeCSV(data)
        elif getForm == 'console':
            data = DisplayData()
            data.printData(getData) 