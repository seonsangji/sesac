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