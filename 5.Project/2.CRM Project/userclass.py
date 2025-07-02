import random
from datetime import datetime as dt




class GenerateUserName:
    
    def __init__(self, file_path):
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, "r", encoding = "utf-8") as file:
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
        self.year = random.randint(1950,2010)

    def generateUserBirthdate(self) -> str :

        month = f"{random.randint(1,12):02d}"
        day = f"{random.randint(1,28):02d}"
        return (  str(self.year) + "-" + str(month) + "-" + str(day)  )

    def generateUserAge(self):
        return int(dt.now().strftime('%Y')) - self.year
        
    # 파일 경로 불러오고,
    # 파일 읽고 랜덤으로 뽑고
    # 뽑은 값 반환한다
class GenerateUserAddress:

    def __init__(self, file_path):
        self.cities = self.load_file_from_data(file_path)

    def load_file_from_data(self, file_path):
        with open ("city.text", "r", encoding = "utf-8") as file:
            data = file.read().splitlines()
            return data

    def generateUserAddress(self):
        self.address = (str(random.randint(1,99)) + " " + random.choice(self.cities))
        return self.address
    



class GenerateUser:

    def __init__(self):
        self.genName = GenerateUserName("name.txt")
        self.genGender = GenerateUserGender()
        self.genBirthdateAndAge = GenerateUserBirthdateAndAge()
        self.genAddress = GenerateUserAddress("city.txt")

    def generateUser(self,count):
        
        for _ in range(count):
            user = []
            user.append(self.genName.generateUserName())
            user.append(self.genGender.generateUserGender())
            user.append(self.genBirthdateAndAge.generateUserBirthdate())
            user.append(self.genBirthdateAndAge.generateUserAge())
            user.append(self.genAddress.generateUserAddress())
            print(user)

test = GenerateUser()
test.generateUser(5)

# 각각 클래스에서 객체 만들고
# users리스트에 객체.메서드로 name, gener, ... 넣기
# 반복문 만들기






