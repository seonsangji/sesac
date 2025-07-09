from abc import ABC, abstractmethod

# 추상 클래스 : 필수로 구현해야 하는 함수를 지정
class Displayable(ABC):
    registry = {}

    def __init_subclass__(cls,**kwargs):
        super().__init_subclass__(**kwargs)
        Displayable.registry[cls] = cls
    
    @abstractmethod
    def display(self):
        pass

class User(Displayable):
    def display(self):
        print("사용자 객체 처리")

class Store(Displayable):
    def display(self):
        print("상점 객체 처리")

class Item(Displayable):
    def display(self):
        print("아이템 객체 처리")

class Order(Displayable):
    def display(self):
        print("주문 객체 처리")

class DisplayData(Displayable):
    def __init__(self, data):
        handler = Displayable.registry.get(type(data))
        if handler:
            data.display()
        else:
            print("지원하지 않는 타입입니다.")
        

DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(Order())
DisplayData(OrderItem())