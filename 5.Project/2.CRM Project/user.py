import random

names= []
cities = []
towns = []


def generate_name():
    return random.choice(names)
#나중에 text에서 뽑기

def generate_birthdate():
    year = random.randint(1950, 2010)
    month = random.randint(1,12)
    day = random.randint(1,28)
    return f"{year}-{month:02d}-{day:02d}"

def generate_gender():
    return random.choices(["Male", "Female"])

def generate_address():
    city = random.choice(cities)
    town = random.choice(towns)
    street_num = random.randint(1,100)
    return f"{city} {street_num}"

