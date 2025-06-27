# 딕셔너리라고 부름


my_dict = { "name" : "Alice", "age" : 25, "location" :"Seoul"}
print(my_dict)

print(my_dict["name"])

user1 = { "name" : "Bob", "age" : 30, "location" :"Busan"}
print(user1["age"])

user1["age"]=31
print(user1["age"])

user1["phone"] = "iPhone 16"
print(user1)

user1["phone"] = ""
print(user1)

del user1["phone"] 
# del을 우리가 키워드로 쓰기 때문에 변수로 쓸수는 없다
print(user1)

# 키워드는 변수명 불가능, 함수명으로도 사용 지양지양
# del = 5
# print = "hello, print"
# print(print)

print(user1.keys())
print(user1.values())
print(user1.items())
