# 파이썬은 변수 지정 키워드 없다

x=5
y=3

print(x/y)
print(x % y)
print(x ** y)

str_x = "100"

# print (x + str_x) 문자와 숫자는 더할 수 없음

int_x = int(str_x) 
# 문자를 숫자(정수)로 변환


# 비트연산자
print(1 & 1)
print(1 & 0)
print(0 & 1)
print(0 & 0)

# 비트연산자 OR
print(1 | 1)
print(1 | 0)

# 주의 기계는 2진수를 사용한다
print(x & y)
print(x | y)