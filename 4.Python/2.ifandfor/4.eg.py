numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 == 0 :
        print(f"숫자 {num}은 짝수입니다.")
    elif num % 2 ==1 :
        print(f"숫자 {num}은 홀수입니다.")

def getEvenNumbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0 :
         even_numbers.append(num)

    return even_numbers

even = getEvenNumbers(numbers)
print(f"짝수는: {even}")

# 다음 목록에서 성적이 A인 학생만 반환하시오.........

    
students = {
    '철수': 70,
    '영희': 82,
    '민수': 88,
    '지은': 75,
    '현우': 93,
    '민정': 67,
    '지민': 76,
    '우성': 99,
    '세훈': 61,
    '지효': 85,
}


for name,score in students.items():
    result = []
    if score >= 90:
        result.append(name)
    return result


