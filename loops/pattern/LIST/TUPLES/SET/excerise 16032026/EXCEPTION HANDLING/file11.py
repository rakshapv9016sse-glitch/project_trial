try:
    f=open("sample.txt","w")
    f.write("heyyy rakshaaaa")
except Exception:
    print("error while wriritng file")
finally:
    f.close()
    print("file closed successfully")
    