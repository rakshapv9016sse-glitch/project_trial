class bus:
    def __init__(self,price):
        self.price=price
    def total(self,persons):
        print("total:",self.price*persons)
a=bus(45)
a.total(50)