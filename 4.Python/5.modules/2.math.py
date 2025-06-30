
import math

print(math.pi)

# pi * radius ^ 2

radius = 5
area = math.pi * radius ** 2
print(f"반지름이 {radius} 인 원의 넓이는 {area}입니도.")

area2 = math.pi * math.pow(radius,2)
print(f"반지름이 {radius} 인 원의 넓이는 {area2:.2f}입니도.") 

text ="Hi"
print(f"[{text:<10}]")
print(f"[{text:^10}]")