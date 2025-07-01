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
        print("활동성이 저하된 생물들에게 유기물을 제공한다")
        for animal in self._animal:
            animal.feed("많은 유기물들")

    



