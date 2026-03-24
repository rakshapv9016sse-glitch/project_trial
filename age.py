age=int(input("enter your age"));
citizen=input("are you a citizen(yes/no)");
if age>=18:
    if citizen=="yes":
        print("eligible to vote");
if age<=18:
    if citizen=="no":
        print("not eligible to vote");
