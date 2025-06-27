name = "Alice"
print(name)
print("Hello", name)
print("Hello," + name)
print("Hello," + name + "!!")


print ("Hello, {}!!".format(name))
print ("Hello, {}!! {}??".format(name, name))

name1 = "Bob"
name2 = "Charlie"
print ("Hello, {1}!! {0}??".format(name1, name2))

print("Hello, %s!!" % name)
print ("Hello, %s!! %s??"% (name1, name2))
#   : %s 문자열을 출력하는 곳이다


# 결론적으로 가장 많이 쓰는 건... f-스트링 표기법 (js ``표기법과 유사)

print(f"Hello, {name}!!")
print(f"Hello, {name1}!! {name2}!!")