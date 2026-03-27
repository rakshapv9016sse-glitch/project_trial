class bank:
    def __init__(self,name,balance):
          self.__name=name
          self.__balance=balance
account=bank("raksha",50000)

class bank:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def get_name(self):
        return self.__name
account=bank("raksha",50000)
print(account.get_balance())
print(account.get_name())
    
    