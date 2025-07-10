import random
from common import GenerateId

class GenerateStoreId(GenerateId):
    pass

from common import GenerateAddress


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

    

class GenerateStore():

    def __init__(self):
        self.genId = GenerateStoreId()        
        self.genName = GenerateStoreName("data/type.txt", "data/region.txt")
        self.genAddress = GenerateStoreAddress("data/city.txt","data/town.txt")

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