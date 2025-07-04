from storeclass import GenerateStore


class DisplayData(GenerateStore):

    def printData(self,count):
        data = self.generateStore(count)
        for id, name, type, address in data:
            print(f"ID: {id}\nName: {name}\nType: {type}\nAddress : {address}\n")

    def saveData(self,count):
        return self.generateStore(count)
    

def generateCSV(count):
    getData = DisplayData()
    return getData.saveData(count)
            
