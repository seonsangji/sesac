from animal import Animal
from cat import Cat
from dog import Dog 
from typing import List


class Farm:

    def __init__(self,name):
        self._animal: List[Animal] = []
        self._name: str=name
    
    def add_animal(self,animal: Animal) -> None:
        self._animal.append(animal)

    def feed_all(self): 
        print("즐거운 식사 시간")
        for animal in self._animal:
            animal.feed("많은 밥")

    def move_all(self):
        print("모든 동물들이 움직이는 중")
        for animal in self._animals:
            animal.move()

    



