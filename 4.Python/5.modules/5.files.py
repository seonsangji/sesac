import os
my_dir = 'sesac1234'

print("hello")

for filename in os.listdir(my_dir):
    file_path = os.path.join(my_dir, filename)
    if (os.path.isfile(file_path)):
        print(filename)
