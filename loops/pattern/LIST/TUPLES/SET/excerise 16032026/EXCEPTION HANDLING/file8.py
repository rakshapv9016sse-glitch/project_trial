try:
    r=int(input("enter number:"))
    print(5/r)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("invalid input")
else:
    print("no error occurred")