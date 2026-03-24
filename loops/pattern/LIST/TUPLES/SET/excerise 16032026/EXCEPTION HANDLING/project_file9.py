try:
    r=int(input("enter the first number:"))
    d=int(input("enter the second number:"))
    print("choose operation: +,-,*,/")
    op=input("enter operation:")

    if op =="+":
        print("result:",r+d)
    elif op=="-":
        print("result:",r-d)
    elif op=="*":
        print("result:",r*d)
    elif op=="/":
        print("result:",r/d)
    else:
        print("invalid operator")
except ZeroDivisionError:
    print("error:zero division error")
except ValueError:
    print("error:value error")
except TypeError:
    print("error:type error")
else:
    print("calculation success")