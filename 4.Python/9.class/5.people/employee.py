from person import Person
from student import Student

alice = Person("ALICE", 23)
bob = Person("Bob", 24)
tom = Student("Tom", 20, "S12345678")
charlie = Employee("Charlie", 30, "Samsung")

class Employee(Person):
    def __init__(self, name, age, company):
        super

    # 메소드 오버라이팅
    def greet(self):
        print(f"저는 {self.company}에서 일하는 {self.name} 입니다.")

    def work(self):
        print(f"직원 {self.name}은 {self.company}에서 일하는 중입니다.")