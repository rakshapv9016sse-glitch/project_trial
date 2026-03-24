try:
    username=input("enter your username:")
    password=input("enter your password:")
    if username=="RAKSHA" and password=="2612":
        print("login successful")
    elif username==""or password=="":
        raise ValueError("empty input not allowed")    
    else:
        print("invalid credentials")
except ValueError as r:
    print("error:",r)
finally:
    print("completed")