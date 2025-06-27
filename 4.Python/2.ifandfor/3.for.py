for i in range(5):
    print(i)

for i in range(1,10):
    print(i)

for i in range(1,10,2):
    print(i)
    # 1부터 10까지 2씩 건너뛴다

for i in range(1,10,3):
    print(i)

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

for i, f in enumerate(fruits):
    print(i, f)
ㄴ
str = "Hello, World!"
for char in str:
    print(char)

count_o = 0
for char in str:
    if char =='o':
        count_o +=1
print(f'{str} 문장 내의 1의 개수는 {count_o}개 입니다.')
