from animal import Animal

class Cat(Animal):
    
    def __init__(self, name, energy=None):
        super().__init__(name, energy)
        
    def speak(self):
        print(f"{self._name} says ... meow")

    def read_energy(self):
        print(f"이 동물의 체력은 현재 {self._energy}입니다.")

    def move(self):
        if self._energy >= 5:
            self._energy = self._energy - 5
            print(f"{self._name}님이 두근두근 이동 중입니다. 현재 체력 : {self._energy}")
        else :
            print("헉헉 이동하기에 체력이 부족합니다. 밥이 피료해요.")

# sangji = Cat("sj")
# sangji.move()
# print(sangji._energy)


