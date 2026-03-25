try:
    correct_pin=2612
    attempts=3
    while attempts>0:
        pin=int(input("enter pin:"))
        if pin==correct_pin:
            print("access granted")
            break
        else:
            attempts-= 1
            print("wrong pin!!.attemtps left:",attempts)
    if attempts==0:
        raise Exception("card blocked")
except ValueError:
    print("invalid PIN format")

except Exception as e:
    print("error",e)