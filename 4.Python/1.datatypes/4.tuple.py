# 튜플 = 리스트와 동일, 그러나 데이터를 변경할 수 없다!!
my_tuple = (1,2,3,4,5)

print(my_tuple[0])

# my_tuple[2] = 5 튜플 데이터는 수정 불가하므로 -> 오류 발생
# 바꾸고 싶다면..

my_list = list(my_tuple)
my_list[2] = 5

my_tuple2 = tuple(my_list)
print(my_tuple2[2])

# 튜플  안에 데이터를 여러개의 변수로 나누어 담을 수 있다 == 튜플 언패킹 !!
a,b,c = (1,2,3)

a,b,_ = (1,2,3)
# 받아와서 안쓸 변수를 파이썬 관행으로 _(밑줄)사용
print(a)

