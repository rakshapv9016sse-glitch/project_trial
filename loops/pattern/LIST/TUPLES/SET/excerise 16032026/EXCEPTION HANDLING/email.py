try:
    email=input("enter your email:")
    if "@" not in email or "." not in email:
        raise Exception("invalid email")
    print("valid email")
except Exception as e:
    print("error:",e)