class cart:
    def __init__(self):
        self.price=0
    def add(self,price):
        self.total=price
    def show(self):
        print("total:",self.total)
c = cart()
c.add(120)
c.add(260)
c.show()