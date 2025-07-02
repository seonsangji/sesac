class 차:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class 자동차(차):

    def 정보(self):
        print("바퀴수", self.wheel)
        print("가격", self.price)

car = 자동차(4, 1000)
car.정보()


class 자전차(차):
    def __init__(self,wheel, price,구동계):
        super().__init__(wheel,price)
        self.구동계 = 구동계


bicycle = 자전차(2,100,"시마노")
print(bicycle.구동계)


class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()