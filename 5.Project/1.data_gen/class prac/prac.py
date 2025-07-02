import random

class Account:


    account=0




    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_list = []
        self.withdraw_list = []

        self.bank = "SC은행"
        self.name = name
        self.balance = balance

        num1 = f"{random.randint(0,999):03d}"
        num2 = f"{random.randint(0,99):02d}"
        num3 = f"{random.randint(0,999999):06d}"
        number = str(num1) + "-" + str(num2) + "-" + str(num3)
        self.number = number

        

        Account.account += 1



        

    @classmethod
    def get_account_num(cls):
        print(cls.account)

  
        

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_list.append(amount)
            
            # amount값 저장

        self.deposit_count +=1

        if self.deposit_count % 5 == 0:
            self.balance = self.balance * 1.01

    def deposit_history(self):
        
        #amount 담는 리스트 만들기
        print(self.deposit_list)

        
        
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            self.withdraw_list.append(amount)

        else : print("잔고가 부족합니다.")


    def withdraw_history(self):
        for _ in self.withdraw_list:
            print(_)

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주:", self.name)
        print("계좌번호:", self.number)
        print("잔고:", format(self.balance,","), "원")










a = Account("sangji", 10)
a1 = Account("sangji1", 10)
a2 = Account("sangji2", 10)
a3 = Account("sangji3", 10)
print(a.name)
print(a.number)
print(a.balance)

a.get_account_num()

a.deposit(30)
a.deposit(30)
a.deposit(30)
a.deposit(30)
print(a.balance)

a.deposit(30)
a.withdraw(30)
print(a.balance)
a.withdraw(20)
a.deposit(100000000)
a.display_info()




# for _ in now_list:
#     if 

a.deposit_history()
print(a.deposit_list)

a.withdraw_history()