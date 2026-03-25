try:
    file_name=input("enter your file name:")
    data=input("enter text:")
    if file_name=="":
       raise Exception("file name cannot be empty!!")
    f=open(file_name,"w")
    f.write(data)
    print("data written successfully")
except Exception as e:
    print("error:",e)
finally:
    try:
        f.close()
        print("file closed")
    except:
        print("file not created")