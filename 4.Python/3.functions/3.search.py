numbers = [1,3,5,7,9,11,13,15,17,19]
def linear_search(numbers,target):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] ==target:
            print("선형탐색에서의 비교횟수: ", count)
            return i
        
    return -1

def binary_search(numbers,target):
    left=0
    right= len(numbers) - 1

    while left <= right:
        mid = (left+right) // 2 
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

target = 17
print(linear_search(numbers,target))
print(binary_search(numbers,target))


