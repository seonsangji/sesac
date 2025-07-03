from userclass import GenerateUser
import sys


class DisplayData(GenerateUser):
    def printData(self, count):
        data = self.generateUser(count)
        for id, name, gender, birthdate, age, address in data:
            print(f"ID: {id}\nName: {name}\nGender: {gender}\nBirthdate: {birthdate}\nAge: {age}\nAddress : {address}\n")

    def printCSV(self,count):
        data = self.generateUser(count)
        
        print("csv에 저장하기")
        return data


# a = DisplayData()
# # a.printData(2)
# print(a.printCSV(2))

class PrintCSV:

    userNum = int(input("user수: "))
    

    generateInputUser = DisplayData()
    # generateInputUser.printCSV(userNum)
    userData = generateInputUser.printCSV(userNum)

# print(userData)



# input 에서 count값 (user 몇명 만들지) 받고 - userNum
# generateUser() : count값만큼 user 생성
# printCSV() : [( , , , , ), ( , , , , )] 형태의 data를 데리고 csv 만들고 write.

    
        
    import csv

    with open ( "users.csv", "w", newline="", encoding="utf-8") as file:
        print(userData)
        for i in range(len(userData)):
            print(userData[i]) 

        csv_writer = csv.writer(file)
        csv_writer.writerow(["id", "이름", "성별", "생년월일", "나이", "주소"])
        csv_writer.writerows(userData)
    


    

    
    # 이때 새 csv 만들기 / 기존 csv에 추가하기로 나누자