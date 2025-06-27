str = "Hello,World"
str2 = "Hello me and myselfff"
print(str)

# 라이브러리 함수로 만들어 놨다
print(str.lower())
print(str2.strip())
print(str2.split())

words = str2.split()
print(words[0])
print(",".join(words))