import csv
import random

from main import GenerateId
from orderclass import GenerateIdFromCSV

class GenerateOrderItemId(GenerateId):
    pass

class GenerateOrderId(GenerateIdFromCSV):
    pass

class GenerateItemId(GenerateIdFromCSV):
    pass

class GenerateOrderItem():

    def __init__(self):
        self.genId = GenerateOrderItemId()
        self.genOrderId = GenerateOrderId("orders.csv")
        self.genItemId = GenerateItemId("items.csv")

    def generateOrderItem(self,count):

        orderItems = []
        for _ in range(count):
            id = self.genId.generateId()
            orderId = self.genOrderId.generateIdFromCSV()
            itemId = self.genItemId.generateIdFromCSV()

            orderItems.append((id, orderId, itemId))

        return orderItems
    
test = GenerateOrderItem()
print(test.generateOrderItem(5))

