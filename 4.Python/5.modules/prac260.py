class Stock:
    def __init__(self, name, code, per, pbr, profit):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.profit = profit


    def set_name(self,name):
        self.name = name
    def set_code(self,code):
        self.code = code
    def set_per(self,per):
        self.per = per
    def set_pbr(self,pbr):
        self.pbr = pbr
    def set_dividend(self,dividend):
        self.dividend = dividend

    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    

samsung = Stock("삼성전자","005930", 15.79, 1.33,2.83)
print(samsung.profit)


samsung.set_per("12.75")

print(samsung.per)


class stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self,name):
        self.name = name
    def set_code(self,code):
        self.code = code
    def set_per(self,per):
        self.per = per
    def set_pbr(self,pbr):
        self.pbr = pbr
    def set_dividend(self,dividend):
        self.dividend = dividend


samsung = Stock("삼성전자","005930",15.79, 1.33, 2.83)
hyundai = Stock("현대차","005380",8.70, 0.35, 4.27)
lg = Stock("LG전자","066570",317.34, 0.69, 1.37)

list = [samsung, hyundai, lg]

for i in list:
    print (i.code, i.per)

class Account:
    def __init__(self, bank, owner, number, asset):
        self.bank = bank
        self.number = number
        self.owner = owner
        self.asset = asset

    def set_bank(self, bank):
         self.bank = bank
    def set_number(self, number):
         self.number = number
    def set_owner(self, owner):
         self.owner = owner
    def set_asset(self, asset):
         self.asset = asset
    
import random

def form_number():
    new_account = Account(None, None, None, None)
    user = input("예금주:")

    new_account.set_owner(user)
    new_account.set_bank("sc은행")

    ran_select = str(random.randint(10**10,10**11-1))
    ran_account = ran_select[:3] + "-" + ran_select[3:5] + "-" + ran_select[5:]
    new_account.set_number(ran_account)

    print(new_account.number)
    
form_number()





    