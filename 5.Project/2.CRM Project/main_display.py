import sys
import csv

class DisplayData(제너레이터상속받음);
    def printData(self,count):
        data = self.제네레이터함수(count)
        반복으로 예쁘게 프린트

    def printCSV(self,count):
        data = self.제네레이터함수(count)
        return data





def generateCSV(count):
    a = DisplayData()
    data = a.printCSV(count)

if __name__ == "__main__": 
        
    num = int(input("생성 수:"))
        
    data = generateCSV(num)



    with open ("해당.csv", "w", newline="", encoding="utf-8") as file:
        
            csv_writer = csv.writer(file)
            csv_writer.writerow(["id", "name", ..헤더명])
            csv_writer.writerows(data)



