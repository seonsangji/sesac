import datetime

print(datetime.datetime.now())

print(type(datetime.datetime.now()))

from datetime import timedelta,datetime

now = datetime.now()
now_date = now.date()

for i in range(5,0,-1):
    delta = timedelta(days=i)
    date = now_date - delta
    print(date)
   
# now = datetime.now()

# for i in range(5,0,-1):
#     delta = timedelta(days=i)
#     date = (now - delta).date()
#     print(date)


from datetime import datetime

print(datetime.now().strftime("%H:%M:%S"))