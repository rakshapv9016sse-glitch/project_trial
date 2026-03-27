class bankaccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def show_info(self):
        print(f"account_number:{self.account_number},balance:{self.balance}")
class savings(bankaccount):
    def __init__(self,account_number,interest_rate,balance):
        super().__init__(account_number,balance)
        self.interest_rate=interest_rate
    def show_bankaccount_info(self):
        print(f"account_number:{self.account_number},balance:{self.balance},interest_rate:{self.interest_rate}")
det=savings(123456789,"2.6%",10000)
det.show_info()
det.show_bankaccount_info()