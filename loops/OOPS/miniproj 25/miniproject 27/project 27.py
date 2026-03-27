class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("amount deposited:",amount)
        else:
            print("invalic amount")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("amount withdrawal:",amount)
        else:
            print("insufficient amount")
class ATM(bankaccount):
    def show_details(self):
        print("n\---account details----")
        print("name:",self.name)
        print("balance:",self.get_balance())

acc=ATM("raksha",2000)
acc.show_details()
acc.deposit(500)
acc.withdraw(400)
acc.show_details()

