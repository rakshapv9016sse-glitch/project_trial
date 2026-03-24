def decorator(func):
    def wrapper(name):
        print("raksha")
        func(name)
        print("prathiba")
    return wrapper
@decorator
def greet(name):
    print(f"vannakam{name}")
greet("!!")