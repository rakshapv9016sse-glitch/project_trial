def decorator(func):
    def wrapper():
        print("raksha")
        func()
        print("prathiba")
    return wrapper
def greet():
    print("hello")
greet=decorator(greet)
greet()