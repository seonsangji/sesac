from cat import Cat
from dog import Dog
from farm import Farm

if __name__ == "__main__":

    dog = Dog("Buddy")
    cat = Cat("Kitty")

    farm = Farm("Sesac")
    farm.add_animal("Buddy")
    farm.add_animal("Kitty")


    dog.speak()
    cat.speak()

    dog.move()
    cat.move()

    for _ in range(10):
        dog.move()

    for _ in range(20):
        cat.move()


# c1 = Cat("m")
# c2 = Cat("e")
# c3 = Cat("o")
# c4 = Cat("w")
# d1 = Dog("w")