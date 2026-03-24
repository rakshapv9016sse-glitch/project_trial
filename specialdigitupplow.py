text="Raksha_26"
upper=0
lower=0
digit=0
special=0
for ch in text:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1
print("lower:",lower)
print("upper:",upper)
print("digit:",digit)
print("special:",special)
    



    