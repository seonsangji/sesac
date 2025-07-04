import random
import uuid
import csv

class GenerateId:

    def generateId(self):
        return str(uuid.uuid4())
    

class GenerateAddress:
    def __init__(self, file_path1, file_path2):
        self.cities = self.load_file_from_data1(file_path1)
        self.towns = self.load_file_from_data2(file_path2)

    def load_file_from_data1(self, file_path1):
        with open (file_path1, "r", encoding = "utf-8") as file:
            data1 = file.read().splitlines()
            return data1
    
    def load_file_from_data2(self, file_path2):
        with open (file_path2, "r", encoding = "utf-8") as file:
            data2 = file.read().splitlines()
            return data2   
    def generateAddress(self):
        self.address = (random.choice(self.cities) + " " + random.choice(self.towns)+ str(random.randint(1,99)) + random.choice(["로", "길"]) + " " + str(random.randint(1,99)))
        return self.address
    
    
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