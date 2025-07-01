numbers = [1,2,3,4,5]


try: 

    first_value = numbers[0]
    print(f"첫번째 숫자는 {first_value} 입니다.")
    last_value = numbers[5]
    print(f"마지막 숫자는 {last_value} 입니다.")
except IndexError:
        print("숫자 잘못 참조 햇어염!")

if first_value and last_value:
      
    diff = last_value - first_value
    print(f"두 수의 차이는 {diff}입니당.")
else:
     print(f"알 수 없는 오류에오.")

