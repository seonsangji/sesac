from userclass import GenerateUser

class DisplayData(GenerateUser):

    def printData(self, count):
        data = self.generateUser(count)
        for id, name, gender, birthdate, age, address in data:
            print(f"ID: {id}\nName: {name}\nGender: {gender}\nBirthdate: {birthdate}\nAge: {age}\nAddress : {address}\n")

    def saveData(self,count):
        return self.generateUser(count)


def generateCSV(count):
    getData = DisplayData()
    return getData.saveData(count)
            





# # input 에서 count값 (user 몇명 만들지) 받고 - userNum
# # generateUser() : count값만큼 user 생성
# # printCSV() : [( , , , , ), ( , , , , )] 형태의 data를 데리고 csv 만들고 write.