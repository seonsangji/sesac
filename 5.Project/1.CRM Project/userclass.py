import random

from datetime import datetime as dt

from common import GenerateId, GenerateAddress


class GenerateUserId(GenerateId):
    pass


class GenerateUserName:
    
    def __init__(self, file_path):
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, "r", encoding= "utf-8") as file:
            data = file.read().splitlines()
        return data

    def generateUserName(self):
        name = random.choice(self.names)
        return name
    

class GenerateUserGender:

    def generateUserGender(self):
        return random.choice(["male", "female"])
    
    
class GenerateUserBirthdateAndAge:

    def __init__(self):
        self.year = self.generateUserBirthyear()

    def generateUserBirthyear(self):
        return random.randint(1950,2010)
    
    def generateUserBirthdate(self) -> str :
        month = f"{random.randint(1,12):02d}"
        day = f"{random.randint(1,28):02d}"
        return (  str(self.year) + "-" + str(month) + "-" + str(day)  )

    def generateUserAge(self):
        return int(dt.now().strftime('%Y')) - self.year
        


class GenerateUserAddress(GenerateAddress):
    pass

class GenerateUser():

    def __init__(self):
        self.genId = GenerateUserId()
        self.genName = GenerateUserName("data/name.txt")
        self.genGender = GenerateUserGender()
        self.genAddress = GenerateUserAddress("data/city.txt","data/town.txt")

    def generateUser(self,count):
        
        users = []
        for _ in range(count):           
            genBirthdateAndAge = GenerateUserBirthdateAndAge()
            id = self.genId.generateId()
            name = self.genName.generateUserName()
            gender = self.genGender.generateUserGender()
            birthdate = genBirthdateAndAge.generateUserBirthdate()
            age = genBirthdateAndAge.generateUserAge()
            address = self.genAddress.generateAddress()
            users.append((id, name, gender, birthdate, age,address))           
        return users
        
# GenerateUser 상속받는 Display 클래스 만들기


# test = GenerateUser()
# print(test.generateUser(5))

# 각각 클래스에서 객체 만들고
# users리스트에 객체.메서드로 name, gener, ... 넣기
# 반복문 만들기



