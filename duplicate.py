text=input("enter a string:")
result=""
for ch in text:
    if ch not in result:
        result+=ch
print("string without duplicates:",result)