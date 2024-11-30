n=input("enter a string:")
list_string=n
newlist=[i for i in list_string.casefold()]
dict={}.fromkeys(newlist,0)
for i in newlist:
    if i in dict:
        dict[i]+=1
        print(list_string)
        print(dict)