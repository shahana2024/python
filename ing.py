n=input("enter the string")
if len(n)>3:
    if n[-3:] !="ing":
        print(n +"ing")
    else:
        print(n+"ly")
else:
    print(n)