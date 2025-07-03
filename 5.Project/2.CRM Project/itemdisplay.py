from itemclass import GenerateItem
import sys
import csv

class DisplayData(GenerateItem):

    def printData(self,count):
        data = self.generateItem(count)
        for id, name, type, price in data:
            print(f"ID: {id}\nName: {name}\nType: {type}\nPrice : {price}\n")

    def saveData(self,count):
        return self.generateItem(count)
        
# a = DisplayData()
# a.printData(5)


def generateCSV(count):
    getData = DisplayData()
    return getData.saveData(count)
            
if __name__ == "__main__": 
    num = int(input("item수:"))
    data = generateCSV(num)

    with open ("items.csv", "w", newline="", encoding="utf-8") as file:

        csv_writer = csv.writer(file)
        csv_writer.writerow(["Id", "Name", "Type", "Price"])
        csv_writer.writerows(data)



generateCSV(5)
