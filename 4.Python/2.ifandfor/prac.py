list = ["dog", "cat", "parrot"]
for i in list:
        print(i.capitalize())

list = ["dog", "cat", "parrot"]
for i in list:
        first = i[0]
        upper_class = first.upper()
        print(upper_class + i[1:])

print()
print("#159")

list = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list:
        print(i.split(".")[0])

list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list:
        if i.split(".")[1] == "h":
            print(i.split("."))


for i in range(0,100,1):
       print(i)


list = range(100)
reverse_list = list[::-1]
for i in reverse_list:
       print(i)

for i in range(99,-1,-1):
       
       print(i)


for i in range(10):
       print(0,1*i)
       

for i in range(1,10,1):
       print(f"3x{i} = {3*i}")


for i in range(1,10,1):
       if i % 2 != 0:
        print(f"3x{i} = {3*i}")
            
print(sum(range(11)))

list = []
for i in range(11):
       list.append(i)
print(sum(list))

hab = 0
for i in range(1,10,2):
       hab += i
print("합:", hab)

gob = 1
for i in range(1,11):
       gob = gob * i
print(gob)

price_list = [32100, 32150, 32000, 32500]
a = -1
for i in range(4):
       a += 1
       print( a, price_list[i])
       

price_list = [32100, 32150, 32000, 32500]

for i in range(4):
       
       print( 3-i, price_list[i])


price_list = [32100, 32150, 32000, 32500]
for i in range(4):
       if (90 + (10*i)) >= 100:
              print((90 + (10*i)),price_list[i] )

my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1):
       print(my_list[i], my_list[(i+1)])


my_list = ["가", "나", "다", "라", "마"]
for i in range(2,len(my_list)):
       print(my_list[i-2], my_list[i-1], my_list[i])

my_list = ["가", "나", "다", "라", "마"]
for i in range(2,len(my_list)) :
       pick = my_list[i-2:(i+1)]

my_list = ["가", "나", "다", "라"]
for i in range(1,len(my_list)):
       print(my_list[len(my_list)-i], my_list[len(my_list)-i-1])

my_list = [100, 200, 400, 800]
for i in range(1,len(my_list)):
       print(my_list[i]-my_list[i-1])


my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(2,len(my_list)):
       print(sum(my_list[i-2:i+1]) / 3)


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):

       volatility.append(high_prices[i] - low_prices[i])
print(volatility)

stock = [ ["시가", "종가"], [100,80],[200,210],[300,330]]

stock = { "시가":[100,200,300], "종가": [80,210,330] }
print(stock)

stock = { "10/10": [80,100,70,90]}

apart = [ [101, 102], [201, 202], [301, 302] ]
for floor in apart:
       for room in floor:
              print(room, "호")
              print("-----")

apart = [ [101, 102], [201, 202], [301, 302] ]
for floor in reversed(apart):
       for room in floor:
              print(room, "호")

print("-------------------------")

print("-"*5)

apart = [ [101, 102], [201, 202], [301, 302] ]
for floor in apart:
       for room in floor:
              print(room, "호")
              if room == floor[1]:
                     print("-----")

apart = [ [101, 102], [201, 202], [301, 302] ]
for floor in apart:
       for room in floor:
              print(room, "호")
print("-----")

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for row in data:
       for col in row:
              print(col*1.00014)
       print("-"*4)

result= []
for row in data:
       for col in row:
              result.append(col*1.00014)
print(result)


data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result= []
for row in data:
       sub = []
       for col in row:
              sub.append(col*1.00014)
       result.append(sub)
print(result)

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for row in ohlc[1:]:
       print(row[3])

volatility=[]
for row in ohlc[1:]:
       volatility.append(row[1]-row[2])
print(volatility)

profit=[]
for row in ohlc[1:]:
       profit.append(row[3]-row[0])
print(sum(profit))


def print_coin():
       print("비트코인")
print_coin()