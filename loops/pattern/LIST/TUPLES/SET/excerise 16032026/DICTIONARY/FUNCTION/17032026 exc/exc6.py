def vowels_number(r):
    count=0
    vowels="aeiou"
    for char in r:
        if char in vowels:
            count+=1
    return count
print(vowels_number("raksha"))
