import csv
import random

from main import GenerateId

class GenerateOrderID(GenerateId):
    pass

class GenerateOrderAt():

    def __init__(self):
        pass

    def generateOrderDate(self) -> str :
        year = 2025
        month = f"{random.randint(1,7):02d}"
        day = f"{random.randint(1,28):02d}"
        return  str(year) + "-" + str(month) + "-" + str(day)   
        
    
    def generateOrderTime(self):
        hour = f"{random.randint(10,22):02d}"
        min = f"{random.randint(0,60):02d}"
        sec = f"{random.randint(0,60):02d}"
        return  str(hour) + ":" + str(min) + ":" + str(sec)  
        
    
class GenerateIdFromCSV():

    def __init__(self,file_path):
        self.data = self.load_file_from_data(file_path)

    def load_file_from_data(self, file_path):
        with open (file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            data = []
            for row in csv_reader:
                data.append(row[0])
            return data
        
    def generateIdFromCSV(self):
        id = random.choice(self.data)
        return id
            
    # 헤더 건너뛸것



# a = GenerateOrderAt()
# print(a.generateOrderDate())

class GenerateOrder():

    def __init__(self):
        self.genId = GenerateOrderID()
        self.genOrderAt = GenerateOrderAt()
        self.genStoreId = GenerateIdFromCSV("stores.csv")
        self.genUserId = GenerateIdFromCSV("users.csv")

    def generateOrder(self,count):

        orders = []
        for _ in range(count):
            id = self.genId.generateId()
            orderAt = f"{self.genOrderAt.generateOrderDate()} {self.genOrderAt.generateOrderTime()}"
            storeId = self.genStoreId.generateIdFromCSV()
            userId = self.genUserId.generateIdFromCSV()

            orders.append((id, orderAt, storeId, userId))
            
        return orders

test = GenerateOrder()
print(test.generateOrder(5))

            
            


    