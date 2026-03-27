class Grandparent:
    def greet_Grandfather(self):
        print("Hello Grandfather!!!")
class Parent(Grandparent):
    def greet_parent(self):
        print("Hello Parent!!!")
class Child(Parent):
    def greet_Child(self):
        print("Hello Child!!!")
a=Child()
a.greet_Grandfather()
a.greet_parent()
a.greet_Child()
