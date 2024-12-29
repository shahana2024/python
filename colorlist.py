color=(input("enter colours separated by comas:"))
color_list1=color.split(',')
print(color_list1)

print("first color:",color_list1[0])
print("last color:",color_list1[-1])
color_list2=["red","orange","black","white"]
print("color list1 not contained in color_list2:")
diff=list(set(color_list1)-set(color_list2))
print(f"the list is{diff}")
color_int_list=[]
for color in color_list1:
    color_int_list.append(len(color))

print(f"list of integers corrensponding to each color:{color_int_list}")