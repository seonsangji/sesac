from common import GenerateId
import json
import random

class GenerateItemId(GenerateId):
    pass


class GenerateMenu:

    def generateMenu(self):

        with open("data/item.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            # print(data)

            category = random.choice(list(data.keys()))
            menu = random.choice(list(data[category].keys()))
            price= data[category][menu]

            return category, menu, price


class GenerateItem():
    
    def __init__(self):
        self.genId = GenerateItemId()
        self.genMenu = GenerateMenu()

    def generateItem(self,count):

        items = []
        
        for _ in range(count):

            id = self.genId.generateId()
            category, menu, price = self.genMenu.generateMenu()
            
            items.append((id, menu, category, price))

        return items

# a = GenerateItem()
# print(a.generateItem(2))