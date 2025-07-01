import random

class NameGenerator:
    def __init__(self, file_path):
        # self.names = ['Jhon', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding = 'utf-8') as file:
            data = file.read().splitlines()
        return data
        

class BirthdateGenerator:
    def generate_birthdate(self):
        day = random.randint(1,28)
        return f"{year}-{month:02d}-{day:02d}"

class UserGenerator:
    def __init__(self):
        self.name_gen

# ------------------

class DisplayData:
    def print_data(self, count):
        data = self.generate_user(count)
        for name, birthdate, gender, address in data:
            print(f"")


