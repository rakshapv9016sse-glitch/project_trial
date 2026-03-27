class person:
    def greet(self):
        print("hellooooo from person")

class student(person):
    def study(self):
        print("student is studyingggg")

class employee(person):
    def work(self):
        print("employee is working")

a=student()
b=employee()
a.greet()
a.study()
b.greet()
b.work()