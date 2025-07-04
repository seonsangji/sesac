import random

from datetime import datetime as dt

from main import GenerateId

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
        
    # 파일 경로 불러오고,
    # 파일 읽고 랜덤으로 뽑고
    # 뽑은 값 반환한다
# class GenerateUserAddress:

#     def __init__(self, file_path1, file_path2):
#         self.cities = self.load_file_from_data1(file_path1)
#         self.towns = self.load_file_from_data2(file_path2)

#     def load_file_from_data1(self, file_path1):
#         with open (file_path1, "r", encoding = "utf-8") as file:
#             data1 = file.read().splitlines()
#             return data1
    
#     def load_file_from_data2(self, file_path2):
#         with open (file_path2, "r", encoding = "utf-8") as file:
#             data2 = file.read().splitlines()
#             return data2
            

#     def generateUserAddress(self):
#         self.address = (random.choice(self.cities) + " " + random.choice(self.towns)+ str(random.randint(1,99)) + random.choice(["로", "길"]) + " " + str(random.randint(1,99)))
#         return self.address
    

from main import GenerateAddress

class GenerateUserAddress(GenerateAddress):
    pass


class GenerateUser():

    def __init__(self):
        self.genId = GenerateUserId()
        self.genName = GenerateUserName("name.txt")
        self.genGender = GenerateUserGender()
        self.genAddress = GenerateUserAddress("city.txt","town.txt")

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






