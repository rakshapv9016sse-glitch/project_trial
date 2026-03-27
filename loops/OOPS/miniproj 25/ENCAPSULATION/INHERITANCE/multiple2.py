class technical:
    def coding(self):
        print("technical skills:coding in python")
class non_technical:
    def management(self):
        print("non technical skills:project management")
class employee(technical,non_technical):
    def __init__(self,name):
        self.name=name
    def showname(self):
        print(f"employee name:{self.name}")

a=employee("raksha")
a.showname()
a.coding()
a.management()