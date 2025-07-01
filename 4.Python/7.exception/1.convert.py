# result = 10 / 0
# print(result)


# try-catch, try-except (modern언어의 오류 처리 방식)
try: 
    result = 10 / 0
    print(result)
except: 
    print("오류: 사탕처럼 달콤하다는데")




def convert_to_int(num_str):
    
    try:
        result = int(num_str)
    except ValueError:
        print("숫자 변하ㅗㄴ에 실패하였습니다. 입력값: ", num_str)
        result = None
    return result



    
# def double_number(num):
#     return num * 2

# user_input = 10
# result = double_number(convert_to_int(user_input))
# print(f"입력한 숫자 : {user_input}의 두배값은 {result}입니다")


