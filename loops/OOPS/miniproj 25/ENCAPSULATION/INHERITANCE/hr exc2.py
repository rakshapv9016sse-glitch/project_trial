class animal:
    def eat(self):
        print("animal eats meat")
class dog(animal):
    def bark(self):
        print("dog barks at strangers")
class cat(animal):
    def meow(self):
        print("cat meows")


a=dog()
b=cat()
a.eat()
a.bark()
b.eat()
b.meow()
