a=int(input("enter first number"));
b=int(input("enter second number"));
c=int(input("enter third number"));
d=int(input("enter fourth number"));
min= a if a<b else b;
minm=min if min<c else c;
minimum=minm  if minm<d else d;
print("minimum number is",minimum);