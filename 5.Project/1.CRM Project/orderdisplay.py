from orderclass import GenerateOrder

import csv

class DisplayData(GenerateOrder):

    def printData(self,count):
        data = self.generateOrder(count)
        for id, orderAt, storeId, userId in data:
            print(f"ID: {id}\nOrderAt: {orderAt}\nstoreId: {storeId}\nUserId : {userId}\n")

    def saveData(self,count):
        return self.generateOrder(count)
    

def generateCSV(count):
    getData = DisplayData()
    return getData.saveData(count)

if __name__ == "__main__":
    num = int(input("order수:"))
    data = generateCSV(num)

    with open("output/orders.csv", "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Id", "OrderAt", "StoreId", "UserId"])
        csv_writer.writerows(data)

# generateCSV(10)