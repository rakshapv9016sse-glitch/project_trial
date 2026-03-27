class student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if 0 <= marks <=100:
            self.__marks=marks 
        else:
            print("invalid marks")

stu=student("raksha",100)
stu.set_marks(50)
stu.set_marks(60)
print(stu.get_marks())