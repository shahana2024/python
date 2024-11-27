dict1={2:"orange",3:"banana",1:"apple"}
print(f"dictionary 1:{dict1}")
l=list(dict1.items())
l.sort()
print('assending order is:',l)
l=list(dict1.items())
l.sort(reverse=True)
print('decending order is:',l)
dict2={4:"plum",5:"cherry"}
print(f"dictionary 2:{dict2}")
dict1.update(dict2)
print(f"dictionary after merging:{dict1}")