from orderitemclass import GenerateOrderItem
import sys
import csv

class DisplayData(GenerateOrderItem):

    def printData(self,count):
        data = self.generateOrderItem(count)
        for id, orderId, itemId in data:
            print(f"ID: {id}\nOrderAt: {orderId}\nstoreId: {itemId}\n")

    def saveData(self,count):
        return self.generateOrderItem(count)
    

def generateCSV(count):
    getData = DisplayData()
    return getData.saveData(count)

if __name__ == "__main__":
    num = int(input("orderitem수:"))
    data = generateCSV(num)

    with open("output/orderitems.csv", "w", newline="", encoding="utf-8") as file:

        csv_writer = csv.writer(file)
        csv_writer.writerow(["Id", "OrderItem", "ItemId"])
        csv_writer.writerows(data)

# generateCSV(10)