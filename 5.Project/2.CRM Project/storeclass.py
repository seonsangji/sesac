import random
import uuid
from main import GenerateId


class GenerateStoreId(GenerateId):
    pass





from main import GenerateAddress


class GenerateStoreAddress(GenerateAddress):
    pass

class GenerateStoreName(GenerateAddress):

    def __init__(self, file_path1, file_path2):
        self.types = self.load_file_from_data1(file_path1)
        self.regions = self.load_file_from_data2(file_path2)

    def generateStoreType(self):
        return random.choice(self.types)
    
    def generateStoreRegion(self):
        return random.choice(self.regions)
    
    def generateStoreName(self):
        type = self.generateStoreType()
        region = self.generateStoreRegion()
        return f"{type} {region}{str(random.randint(1,9))}호점"

    

# a=[]
# b = GenerateStore("store.txt","region.txt")
# c = GenerateStoreAddress("city.txt","town.txt")
# a.append(b.generateStoreName())
# print(a)
# a.append(c.generateAddress())
# print(a)

# class GenerateStore:

#     def __init__(self,file_path1, file_path2):
#         self.types = self.load_file_from_data1()
#         self.regions = self.load_file_from_data2()

#     def load_file_from_data1(self,file_path1):
#         with open (file_path1, "r", encoding= "utf-8") as file:
#             data1 = file.read().splitlines()
#         return data1
    
#     def load_file_from_data2(self, file_path2):
#         with open (file_path2, "r", encoding = "utf-8") as file:
#             data2 = file.read().splitlines()
#             return data2
    
#     def generateStoreType(self):
#         return random.choice(self.types)
    
#     def generateStoreRegion(self):
#         return random.choice(self.regions)
    
#     def generateStoreName(self):
#         type = self.generateStoreType()
#         region = self.generateStoreRegion()
#         return f"{type} {region}{str(random.randint(1,9))}호점"
    






class GenerateStore():

    def __init__(self):
        self.genId = GenerateStoreId()
        
        self.genName = GenerateStoreName("type.txt", "region.txt")

        self.genAddress = GenerateStoreAddress("city.txt","town.txt")

    def generateStore(self,count):
        
        stores = []
        for _ in range(count):           

            id = self.genId.generateId()
            name = self.genName.generateStoreName()
            type = name.split()[0]
            address = self.genAddress.generateAddress()
            stores.append((id,name, type, address))
            
        return stores
    
# a = GenerateStore()
# print(a.generateStore(2))