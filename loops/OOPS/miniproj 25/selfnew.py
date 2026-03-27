class student:
    def __init__(self,mark):
        self.mark=mark
    def update(self,newmark):
        self.mark=newmark
    def show(self):
        print("mark:",self.mark)
s1=student(50)
s1.show()
s1.update(90)
s1.show()