from animal import Animal

class Panda(Animal):
    def __init__(self, name, energy=None):
        super().__init__(name, energy)
    
    def speak()  -> None:
        print(f"수줍은 {self._name}은/는 마음을 열기에 시간이 걸립니다")

    def move(self):
    if self._energy >= 10:
        self._energy = self._energy - 10
        print(f"{self._name}님이 나풀나풀 이동 중입니다. 현재 체력 : {self._energy}")
    else :
        print("헉헉 이동하기에 체력이 부족합니다. 밥이 피료해요.")