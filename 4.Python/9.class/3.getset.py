
class Person:


    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name


    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age >= 0:
            self.__age = age
        else:
            print("나이는 0보다 커야 합니다")

    def greet(self):
        print(f"안녕하세여, 저는 {self.__name}입니다")

    def ride_car(self):
        print(f"사람이 난폭운전을 하고 있습니다")

sangji = Person("김태희",22)
pongjja = Person("김태희",21)

pongjja.set_age (100)
print(pongjja.get_age())

sangji.name= "신민아"
print(sangji.name)

pongjja.set_age (-100)