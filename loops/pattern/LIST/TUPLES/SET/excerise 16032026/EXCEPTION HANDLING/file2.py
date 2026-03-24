try:
    r=int(input("enter the first number:"))
    d=int(input("enter the second number:"))
    print("result:",r/d)
except ZeroDivisionError:
    print("error:cannot divide by zero")
