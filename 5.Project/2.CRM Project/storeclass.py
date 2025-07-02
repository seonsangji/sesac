import random
import uuid


class GenerateStoreId:

    def generateStoreId(self):
        return str(uuid.uuid4())

class GenerateStore:

    def __init__(self,file_path1, file_path2):
        self.types = self.load_file_from_data1()
        self.regions = self.load_file_from_data2()

    def load_file_from_data1(self,file_path1):
        with open (file_path1, "r", encoding= "utf-8") as file:
            data1 = file.read().splitlines()
        return data1
    
    def load_file_from_data2(self, file_path2):
        with open (file_path2, "r", encoding = "utf-8") as file:
            data2 = file.read().splitlines()
            return data2
    
    def generateStoreType(self):
        return random.choice(self.types)
    
    def generateStoreRegion(self):
        return random.choice(self.regions)
    
    def generateStoreName(self):
        type = self.generateStoreType()
        region = self.generateStoreRegion()
        return f"{type} {region}{str(random.randint(1,9))}호점"
    

class GenerateStoreAddress:

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
            

    def generateStoreAddress(self):
        self.address = (random.choice(self.cities) + " " + random.choice(self.towns)+ str(random.randint(1,99)) + random.choice(["로", "길"]) + " " + str(random.randint(1,99)))
        return self.address
    
    