password=input("enter your password:")
if len(password)<6:
    raise Exception("try another password!!")
print("accepted")