import random

from common import GenerateId, GenerateIdFromCSV

class GenerateOrderID(GenerateId):
    pass

class GenerateOrderAt():

    def __init__(self):
        pass

    def generateOrderDate(self):
        year = 2025
        month = f"{random.randint(1,7):02d}"
        day = f"{random.randint(1,28):02d}"
        return  str(year) + "-" + str(month) + "-" + str(day)   
        
    
    def generateOrderTime(self):
        hour = f"{random.randint(10,22):02d}"
        min = f"{random.randint(0,59):02d}"
        sec = f"{random.randint(0,59):02d}"
        return  str(hour) + ":" + str(min) + ":" + str(sec)  
        
    
# a = GenerateOrderAt()
# print(a.generateOrderDate())

class GenerateOrder():

    def __init__(self):
        self.genId = GenerateOrderID()
        self.genOrderAt = GenerateOrderAt()
        self.genStoreId = GenerateIdFromCSV("output/stores.csv")
        self.genUserId = GenerateIdFromCSV("output/users.csv")

    def generateOrder(self,count):

        orders = []
        for _ in range(count):
            id = self.genId.generateId()
            orderAt = f"{self.genOrderAt.generateOrderDate()} {self.genOrderAt.generateOrderTime()}"
            storeId = self.genStoreId.generateIdFromCSV()
            userId = self.genUserId.generateIdFromCSV()

            orders.append((id, orderAt, storeId, userId))
            
        return orders

# test = GenerateOrder()
# print(test.generateOrder(5))

            
            


    