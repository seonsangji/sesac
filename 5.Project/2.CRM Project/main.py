import csv

def getInput():
    getNum = int(input("생성할 데이터 개수를 입력하세요 (숫자로):"))
    getForm = input("아웃풋 형태를 입력하세요 (csv, console):").lower()
    return getNum, getForm

headers = {
    "users" : ["Id", "Name", "Gender", "Birthdate", "Age", "Address"],
    "stores" : ["Id", "Name", "Type", "Address"],
    "items" :   ["Id", "Name", "Type", "Price"]
}


def outputCSV(file_path, header, data):
    with open (file_path, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(data)


def output(getNum, getForm, file_path, header, data):
    
    if getForm == "csv":
        data = generateCSV(getNum)
        outputCSV(file_path, header, data)

    elif getForm == "console":
        data = DisplayData()
        data.printData(getNum)



while True:
    dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item):").lower()

    if dataType == "user" :
        from userdisplay import generateCSV, DisplayData
        getNum, getForm = getInput()
        data = generateCSV(getNum)
        output(getNum, getForm,"output/users.csv", headers["users"], data)
        break

    elif dataType == "store" :
        from storedisplay import generateCSV, DisplayData
        getNum, getForm = getInput()
        data = generateCSV(getNum)
        output(getNum, getForm,"output/stores.csv", headers["stores"], data)
        break

    elif dataType == "item" :
        from itemdisplay import generateCSV, DisplayData
        getNum, getForm = getInput()
        data = generateCSV(getNum)
        output(getNum, getForm,"output/items.csv", headers["items"], data)
        break
    
    else : 
        print("데이터 유형이 존재하지 않습니다. 다시 시도하세요.")

