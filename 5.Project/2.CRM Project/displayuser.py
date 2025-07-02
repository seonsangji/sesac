from userclass import GenerateUser


class DisplayData(GenerateUser):
    def printData(self, count):
        data = self.generateUser(count)
        for id, name, gender, birthdate, age, address in data:
            print(f"ID: {id}\nName: {name}\nGender: {gender}\nBirthdate: {birthdate}\nAge: {age}\nAddress : {address}\n")

    def printCSV(self,count):
        data = self.generateUser(count)
        print("csv에 저장하기")


a = DisplayData()
a.printData(1)

