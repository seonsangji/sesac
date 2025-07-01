# https://docs.python.org/ko/3.10/library/datetime.html

import datetime

import datetime as dt


print(dt.MINYEAR)
print(dt.MAXYEAR)

print(dt.datetime.now())
print(dt.datetime.now().strftime('%Y-%m-%d'))
print(dt.datetime.now().strftime('%H-%M-%S'))

# 현재 시간을 담은 dt 이라는 개체
my_time = dt.datetime(2025,6,30,10,45,00)
print(type(my_time))
print(my_time)



