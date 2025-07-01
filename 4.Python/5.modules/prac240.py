import datetime

print(datetime.datetime.now())

print(type(datetime.datetime.now()))

from datetime import timedelta,datetime

now = datetime.now()
now_date = now.date()

for i in range(5,0,-1):
    delta = timedelta(days=i)
    date = now_date - delta
    print(date)
   
# now = datetime.now()

# for i in range(5,0,-1):
#     delta = timedelta(days=i)
#     date = (now - delta).date()
#     print(date)


from datetime import datetime

print(datetime.now().strftime("%H:%M:%S"))

import datetime

day ="2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret,type(ret))


from os import getcwd

print(getcwd())

from os import rename, path

print(path.abspath("test.txt"))



# import numpy as np

# print(np.arange(0.0,5.1,0.1))


class Human:
    print("응애응애")

areum = Human()

class Human:
    def __init__(self):
        print("응애")
a = Human()
# b = Human(242)

class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("아름", 25, "여자")
print(areum.name)


print(f"이름: {areum.name}, 나이: {areum.age}, 성별: {areum.gender}")


class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.gender))

areum = Human("아름", 25, "여자")
areum.who()

class Human:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("나의 죽음을 알리지 말라")

    def who(self):
        print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}")

    def setInfo (self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

  

areum = Human("불명", "미상", "모름")
areum.who()

areum.setInfo("아름", 25, "여자")
areum.who()

del areum



class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def who(self):
        print("주식명:{}, 종목명:{}". format(self.name, self.code))
        
    def set_name(self,name):
        self.name = name
    
    def set_code(self,code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

      

samsung = Stock("삼성전자", "005930")
samsung.who()
print(samsung.name)

a = Stock(None, None)
a.set_name("하이닉스")
print(a.name)

a.set_code("005931")
print(a.code)


print(samsung.get_name())