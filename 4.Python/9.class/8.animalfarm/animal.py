class Animal:
    def __init__(self, name : str, energy=None):
        self._name = name
        self._energy = 100

    def get_name(self):
        return self._name
    
    def set_name(self, name: str):
        self._name = name

    def get_energy(self):
        return self._energy
    
    def set_energy(self, energy:int):
        self._energy = energy

    def speak(self):
        print(f"{self._name}이/가 처량하게 울고 있습니다")

    def move(self):
        print(f"{self._name}이/가 날뛰고 있습니다")

    def feed(self, food:str) -> None:
        self._energy += 50
        print(f"{self._name} 은 {food} 를 함냐함냐 먹고 있습니다. 현재 에너지 : {self._energy}")


animal = Animal("sangji")
print(animal._name)
print(animal._energy)

animal.move()

