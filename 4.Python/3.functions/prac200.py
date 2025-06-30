print("hello")

def print_coin():
    print("비트코인")



def print_coins():
    for i in range(100):
        print_coin()

print_coins()

def function(a):
    print(a)

function("hello")

def function2(b):
    print(b)

def print_with_smile(string):
   
    print(f"{string}:D")

print_with_smile("안녕하세요")


def print_upper_price(variable):
    print(variable*1.3)

print_upper_price(3000)

def print_sum(a,b):
    print(a+b)

print_sum(3,4)

def print_arithmetic_operation(a, b):
    print( f"{a} + {b} = {a+b}")
    print( a - b)
    print( a * b)
    print( a / b)

print_arithmetic_operation(3, 4)


def print_max(a,b,c):
    print(max(a,b,c))

print_max(1,2,3)

def print_max(a,b,c):
    if (a >= b) and (a >= c):
        print (a)
    elif (b >= a) and (b>=c):
        print(b)
    else :
        print(c)

print_max(10,0,2)


def print_max(a,b,c):
    max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)

    
print_max(-0.5,-4,-3)

def print_reverse(string):
    print(string[::-1])


print_reverse("python")


def print_score (list):
    print(sum(list) / len(list))

print_score([1,2,3])

def print_even(list):
    for i in list:
        if i % 2 == 0:
            print(i)

print_even ([1, 3, 2, 10, 12, 11, 15])


def print_keys(dic):
    for keys in dic.keys():
        print(keys)


def print_value_by_key ( dic, date):
    for keys in dic.keys():
        if keys == "date":
            print()

def print_5xn(string):
    for i in range(0,len(string),5):
        if i +5 <= len(string):
            print(string[i:i+5])
        else :
            print(string[i:len(string)])

print_5xn("아이엠어보이유알어걸")

print_5xn("아이엠어보이유알어걸호우")

def printmxn(string, num):
    for i in range(0,len(string),num):
        if i +num <= len(string):
            print(string[i:i+num])
        else :
            print(string[i:len(string)])

printmxn("아이엠어보이유알어걸", 3)

def calc_monthly_salary (annual_salary):
    monthly_salary = annual_salary // 12
    return monthly_salary
result = calc_monthly_salary(120_000_000)
print(result)




def make_url(string):
    url = f"www.{string}.com"
    return url

naver_url = make_url("naver")
print(naver_url)


def make_list(string):
    alphabet=[]
    for i in range(len(string)):
        alphabet.append(string[i])
    return alphabet


print(make_list("abcd"))


def pickup_even(list):
    even_list = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even_list.append(list[i])
    return even_list

print(pickup_even([3, 4, 5, 6, 7, 8]))


def convert_int(user):
    
    print(int(user.replace(',','')))


convert_int("1,234,567")


   



