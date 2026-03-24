try:
    r=int(input("enter a number:"))
    print("you entered:",r)
except ValueError:
    print("error:invalid input,please enter a num!!")