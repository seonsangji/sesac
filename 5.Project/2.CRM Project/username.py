import random

def generateUserAddress():
    streetNum = random.randint(1,99)
    with open ("city.text","r", encoding="utf-8") as file:
        data = file.read().splitlines()
        city = random.choice(data)
    address = str(streetNum) + " " + city
    return address

print(generateUserAddress())