from storeclass import GenerateStore

import csv

class DisplayData(GenerateStore):

    def printData(self,count):
        data = self.generateStore(count)
        for id, name, type, address in data:
            print(f"ID: {id}\nName: {name}\nType: {type}\nAddress : {address}\n")

    def saveData(self,count):
        return self.generateStore(count)
    

def generateCSV(count):
    getData = DisplayData()
    return getData.saveData(count)
            
# if __name__ == "__main__": 
#     num = int(input("store수:"))
#     data = generateCSV(num)

#     with open ("stores.csv", "w", newline="", encoding="utf-8") as file:

#         csv_writer = csv.writer(file)
#         csv_writer.writerow(["Id", "Name", "Type", "Address"])
#         csv_writer.writerows(data)

# generateCSV(5)