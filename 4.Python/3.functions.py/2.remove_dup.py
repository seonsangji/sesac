def remove_duplicate(numbers):
    unique_numbers = []
    
    for num in numbers:
        seen_num = False

def remove_duplicate3(number):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    
    return unique_numbers


def remove_duplicate3(number):
    return list(set(number))

numbers = [1,2,3,4,3,2,1,5,6,7,6,5]


print(remove_duplicate(numbers))