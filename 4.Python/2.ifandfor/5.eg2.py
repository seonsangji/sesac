users = [
    {"name":"Alice","age":"25","location":"Seoul","car":"BMW"},
    {"name":"Bob","age":"30","location":"Busan","car":"Mercedes"},
    {"name":"Bob","age":"40","location":"Jeju","car":"Mercedes"},
    {"name":"Charlie","age":"35","location":"Daegu","car":"Audi"},
]

def find_user(name):
    for u in users: 
        if u["name"] == name:
            return u
print(find_user("Alice"))


def find_users(name):
    result = []
    for u in users: 
        if u["name"] == name:
            result.append(u)

    return result

def find_users(name):
    result = []
    for u in users: 
        if u["name"].lower == name.lower():
            result.append(u)

    return result

print(find_user("BoB"))

def find_user2(name,age):
    for u in users:
        if u["name"].lower == name.lower() and u["age"] == age:
            return u
        
print(find_user2("Alice",25))

print('------------find_user3---------------')
def find_user3(name=None,age=None):
    result = []

    for u in users:
        if name:
            if u["name"] == name:
                if age:
                    if u["age"]==age:
                        result.append(u)
                else:
                    result.append(u)
        elif age:
            if u["age"]==age:
                result.append(u)
            
    
        else:
            result.append(u)

    return result

print(find_user3("Bob"))



print('------------------refined_user3---------------')

def find_user3(name=None,age=None):

    result = []

    for u in users:
        if name is not None and age is not None:
            if u["name"]==name and u["age"]==age:
                result.append(u)

        elif name is not None:
            if u["name"]==age:
                result.append(u)


        elif age is not None:
            if u["age"]==name:
                result.append(u)
                
        else:
            result.append(u)

    return result

print(find_user3(name='Bob'))


