my_list = [1,2,3,4,5]
print(my_list)

print(len(my_list))
print(my_list[0])
print(my_list[-1])
# 거꾸로 갈 수 있다 -파이썬 특이점.

# 리스트 슬라이싱
print(my_list[1:3]) 

print(my_list[:2])
# 시작부터 


print('-'*10)

my_list.append(6)

print(my_list)
my_list.insert(2,10) 
# 인덱스2 위치에 숫자 10을 추가하겟다
print(my_list)

another_list = [7,8,9]
print(another_list)
print(my_list)

my_list.extend(another_list)
print(my_list)
print(another_list)

my_list.remove(10)
print(my_list)

my_list.pop(3) 
# 인덱스3에 있는 요소를 삭제할거야
print(my_list)

my_list.pop() 
# 인자를 안주면 마지막 요소 삭제
print(my_list)

my_list.clear()
# 리스트 통째로 ㄹ비우기
print(my_list)

# 리스트 검색
print('-'*10)
my_list = [1,2,3,4,5,3,2,1]

index_of_3 = my_list.index(3) 
# 숫자 3의 인덱스(위치)는 어디

print(index_of_3)

count_2 = my_list.count(2)
# 2라는 숫자는 몇개나 잇나

print(my_list)
sorted_list = sorted(my_list)
# 이거는 인자를 받아서 반환하는 함수 (원본을 변경하지 않음)


print('-'*10)
my_list = [1,2,3,4,5,3,2,1]

my_list.sort()
# 일부 함수는, 복제본을 만들어서 반환하는 애가 있고, 원본 데이터를 고치는 애가 있다.....
# 기본은 오름차순
print(my_list)

my_list.sort(reverse=True)
# 내림차순
print(my_list)

my_list.reverse()
# 현재 리스트를 역순으로 전환
print(my_list)

# 리스트복제
my_list2 = my_list.copy()
print(my_list2)

numbers = [x    for x in range(10)]
print(numbers)

numbers = [num   for num in range(1,11)]
print(numbers)
# 1부터 10까지 숫자들을 만들어 리스트에 채우시오.

numbers = [num**2 for num in range(1,11)]
# 1부터 10까지의 수를 만들어서 그 제곱수로 채우시오.

numbers = [num   for num in range(1,11)      if num % 2 == 0]
# 1부터10까지의 수 중 짝수인 것들로만 리스트를 채우시오.

