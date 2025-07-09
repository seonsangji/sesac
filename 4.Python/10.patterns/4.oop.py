class User:
    def display(self):
        print("사용자 객체 처리")

class Store:
    def display(self):
        print("상점 객체 처리")

class Item:
    def display(self):
        print("아이템 객체 처리")

class DisplayData:
    def __init__(self, data):
        data.display()
        

DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(123)