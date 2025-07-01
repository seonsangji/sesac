from animal import Animal

class Dog(Animal):
    
    def __init__(self, name, energy=None):
        super().__init__(name, energy)
        
    def speak(self):
        print(f"{self._name} says ... woof")

    def read_energy(self):
        print(f"이 동물의 체력은 현재 {self._energy}입니다.")

    def move(self):
        if self._energy >= 10:
            self._energy = self._energy - 10
            print(f"{self._name}님이 나풀나풀 이동 중입니다. 현재 체력 : {self._energy}")
        else :
            print("헉헉 이동하기에 체력이 부족합니다. 밥이 피료해요.")


