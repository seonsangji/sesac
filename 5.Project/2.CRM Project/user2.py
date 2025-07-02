import random

from datetime import datetime as dt

# - M1. 10명의 사람의 이름을 랜덤으로 생성하시오. (영문 이름 샘플 10개 참조해서)
# - M1-2. 성별, 생년월일, 나이를 랜덤으로 생성하시오. (나이 주의 = 생년월일 기반 계산)
# - M1-3. 주소를 랜덤으로 생성하시오.



class User:

    def __init__(self):
        pass

    # def __init__(self, name, gender, age, birthdate):
    #     self.name = None
    #     self.gender = None
    #     self.age = None
    #     self.birthdate = None

    def generateUserName(self):
        with open("name.txt", 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
        return random.choice(data)

    def generateUserGender(self):
        return random.choice(["male","female"])
    
    def generateUserBirthdate(self)-> str :
        year = random.randint(1950,2010)
        self.year = year

        month = f"{random.randint(1,12):02d}"
        day = f"{random.randint(1,28):02d}"
        birthdate = str(year) + "-" + str(month) + "-" + str(day)
        self.birthdate = birthdate
        return self.birthdate
    
    def generateUserAge(self) -> int :
        self.age = int(dt.now().strftime('%Y')) - self.year
        # print("나이뽑아내기")
        return self.age
    

# 대구 강서구 59길 66

    def generateUserAddress(self):
        streetNum = random.randint(1,99)
        with open ("city.text","r", encoding="utf-8") as file:
            data = file.read().splitlines()
            city = random.choice(data)
        address = str(streetNum) + " " + city
        return address


# userInfo = []
# u = User()
# userInfo.append(u.generateUserName())
# userInfo.append(u.generateUserGender())
# userInfo.append(u.generateUserBirthdate())
# userInfo.append(u.generateUserAge())
# userInfo.append(u.generateUserAddress())

def generateUser():

    userInfo = []
    u = User()
    userInfo.append(u.generateUserName())
    userInfo.append(u.generateUserGender())
    userInfo.append(u.generateUserBirthdate())
    userInfo.append(u.generateUserAge())
    userInfo.append(u.generateUserAddress())

    print(userInfo)


for _ in range(10):
    generateUser()
