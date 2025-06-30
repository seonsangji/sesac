import random as ran

print("랜덤 숫자: ", ran.randint(1,1000))
# 1과 1000을 포함하여 랜덤 숫자 생성

def roll_dice():
    number = ran.randint(1,6)
    return number


print(f"주사위 던진 결과: {roll_dice()}")


def roll_dice_again (times):
    my_dic = { "1":0,
               "2":0, 
               "3":0, 
               "4":0, 
               "5":0, 
               "6":0}
    
    for keys in my_dic.keys():
                
            for i in range(1,times): 
                    result = roll_dice()
                    if result == int(keys):
                        keys[result-1] += 1
            

    print(f"{keys}가 나온 횟수: {times}번, 확률: {my_dic[keys] / times}")

roll_dice_again(1000)


counts2 = {i: 0  for i in range(1,7)}
      
def roll_dices2(numbers):
      for i in range(numbers):
            result = roll_dice()
            counts2[result] += 1