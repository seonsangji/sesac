
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}"
    # 나 객체를 person이라고 찍으시오. (원래 객체만 프린트하면 주소를 바인딩)
    
    def greet(self):
        print(f"안녕하세여, 저는 {self.name}입니다")

    def ride_car(self):
        print(f"사람이 난폭운전을 하고 있습니다")

    def __eq__(self,other):
        return self.name ==other.name and self.age ==other.age

sangji = Person("김태희",22)
print(sangji)

pongjja = Person("김태희",21)
pongjja2 = Person("김태희", 21)
pongjja.greet()
pongjja.ride_car()

print(sangji == pongjja)

print(pongjja == pongjja2)
# 서로 다른 객체이므로 --> false
# __eq__ 로 같은 객체로 취급하게 할 수 잇당

