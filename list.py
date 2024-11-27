color=input("enter the colors separated with commas:")
color_list1 = color.split(',')
print(color_list1)

print("first color:",color_list1[0])
print("last color:",color_list1[-1])
color_list2=["red","orange","black","white"]
print("color list1 not contained in list2 are:")
diff=list(set(color_list1)-set(color_list2))
print(diff)
color_in_list=[]
for color in color_list1:
    color_in_list.append(len(color))
print(f"list integers corresponding to each color:{color_in_list}")
