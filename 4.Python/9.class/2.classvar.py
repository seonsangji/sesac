
class Person:
    __count = 0 
    # 클래스 변수
    # __ 으로 private 설정

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.__count += 1 
        # 클래스 변수에 접근하지 위해서는 count +=1 안돼고 객체.변수!!  로컬/클래스 차이..

    def greet(self):
        print(f"안녕하세여, 저는 {self.name}입니다")

    def ride_car(self):
        print(f"사람이 난폭운전을 하고 있습니다")


    #내부 변수에 저장/값 읽어오고 싶다 : getter ex.get_name()
    #내부 변수에 셋팅하고 싶다 : set_name

    @classmethod
    def get_count(cls):
        return cls.__count

sangji = Person("김태희",22)
print(f"만들어진 사람 수: {sangji.get_count}")

pongjja = Person("김태희",21)
print(f"만들어진 사람 수: {pongjja.get_count}")