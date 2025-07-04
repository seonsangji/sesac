
import csv

def getInput():
    getData = int(input("생성할 데이터 개수를 입력하세요 (숫자로):"))
    getForm = input("아웃풋 형태를 입력하세요 (csv, console):").lower()
    return getData, getForm

headers = {
    "users" : ["Id", "Name", "Gender", "Birthdate", "Age", "Address"]
}


def outputCSV(file_path, header, data):
    with open (file_path, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)

            # from userdisplay import generateCSV
            # data = generateCSV(getData)
def output(file_path, header, data):
    getData, getForm = getInput()
    if getForm == "csv":
        data = generateCSV(getData)
        outputCSV(file_path, header, data)
    elif getForm == "console":
        data = DisplayData()
        data.printData(getData)


while True:
    dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item):").lower()

    if dataType == "user" :

        from userdisplay import generateCSV, DisplayData
        getData, getForm = getInput()
        data = generateCSV(getData)
        output("users.csv", headers["users"], data)
        break

    elif dataType == "store" :
        from storedisplay import generateCSV
        getData = int(input("생성할 데이터 개수를 입력하세요 (숫자로):"))
        getForm = input("아웃풋 형태를 입력하세요 (csv, console):").lower()

        if getForm == 'csv':
            from storedisplay import generateCSV
            data = generateCSV(getData)

            with open ("stores.csv", "w", newline="", encoding="utf-8") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(["Id", "Name", "Type", "Address"])
                csv_writer.writerows(data)
            
        elif getForm == 'console':
            from storedisplay import DisplayData
            data = DisplayData()
            data.printData(getData)
        break

    elif dataType == "item" :
        from itemdisplay import generateCSV
        getData = int(input("생성할 데이터 개수를 입력하세요 (숫자로):"))
        getForm = input("아웃풋 형태를 입력하세요 (csv, console):").lower()

        if getForm == 'csv':
            from itemdisplay import generateCSV
            data = generateCSV(getData)

            with open ("items.csv", "w", newline="", encoding="utf-8") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(["Id", "Name", "Type", "Price"])
                csv_writer.writerows(data)
            
        elif getForm == 'console':
            from itemdisplay import DisplayData
            data = DisplayData()
            data.printData(getData)
        break
    
    else : 
        print("데이터 유형이 존재하지 않습니다. 다시 시도하세요.")








# input("아웃풋 형태를 입력하세요 (csv, console):")
# dataForm = sys.argv[3]

# dataNum = generateCSV()

# from userdisplay import generateCSV
# from storedisplay import generateCSV