import random
import uuid

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
    
