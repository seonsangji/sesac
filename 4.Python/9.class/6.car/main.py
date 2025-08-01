from driver import Driver
from car import Car

driver = Driver("Bob", 40, "1종 보통")

driver.drive(30)

car = Car("Tesla", "model s")

driver.assign_car(car)

driver.drive(50)
driver.drive(199)

car.update_odometer(100)

car.update_odometer(300)
car.read_odometer()

car2 = Car("Hyundai", "K5")
driver2 = Driver("David", 30, "2종 보통", car2)
driver2.drive(500)