class bankaccount:
    def account(self):
        print("account number :1234567890")
class savings_account(bankaccount):
    def interest_rate(self):
        print("Interest rate:2.6%")
class premium_savings(bankaccount):
    def amount(self):
        print("minimum amount is 20000")
class current_account(savings_account,premium_savings):
    def balance(self):
        print("balance amount is 200")

a=savings_account()
b=premium_savings()
c=current_account()
a.account()
a.interest_rate()
b.account()
b.amount()
c.account()
c.balance()