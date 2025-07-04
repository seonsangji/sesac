from itemclass import GenerateItem


class DisplayData(GenerateItem):

    def printData(self,count):
        data = self.generateItem(count)
        for id, name, type, price in data:
            print(f"ID: {id}\nName: {name}\nType: {type}\nPrice : {price}\n")

    def saveData(self,count):
        return self.generateItem(count)
            
# a = DisplayData()
# a.printData(5)


def generateCSV(count):
    getData = DisplayData()
    return getData.saveData(count)
            




# generateCSV(5)
