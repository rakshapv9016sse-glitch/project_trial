class person:
    def greet(self):
        print("hellooooo from person")
class student(person):
    def study(self):
        print("student is studying")
class employee(person):
    def work(self):
        print("employee works in office")
class intern(student,employee):
    def int_ern(self):
        print("an intern works as both a student and employee")

a=student()
b=employee()
c=intern()
a.greet()
a.study()
b.greet()
b.work()
c.greet()
c.int_ern()