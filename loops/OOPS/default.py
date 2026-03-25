class student:
    def __init__(self,name="unknown",marks=0):
        self.name=name
        self.marks=marks
r=student()
d=student("raksha",90)
print(r.name,":",r.marks)
print(d.name,":",d.marks)