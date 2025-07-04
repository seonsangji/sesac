import csv




while True:
    dataType = input("데이터 유형을 입력하세요 (User, Store 또는 Item):").lower()

    if dataType == "user" :
        getData = int(input("생성할 데이터 개수를 입력하세요 (숫자로):"))
        getForm = input("아웃풋 형태를 입력하세요 (csv, console):").lower()

        if getForm == 'csv':
            from userdisplay import generateCSV
            data = generateCSV(getData)

            with open ("output/users.csv", "w", newline="", encoding="utf-8") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(["Id", "Name", "Gender", "Birthdate", "Age", "Address"])
                csv_writer.writerows(data)
            
        elif getForm == 'console':
            from userdisplay import DisplayData
            data = DisplayData()
            data.printData(getData)
            
        break

    elif dataType == "store" :
        from storedisplay import generateCSV
        getData = int(input("생성할 데이터 개수를 입력하세요 (숫자로):"))
        getForm = input("아웃풋 형태를 입력하세요 (csv, console):").lower()

        if getForm == 'csv':
            from storedisplay import generateCSV
            data = generateCSV(getData)

            with open ("output/stores.csv", "w", newline="", encoding="utf-8") as file:
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

            with open ("output/items.csv", "w", newline="", encoding="utf-8") as file:
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

    

    