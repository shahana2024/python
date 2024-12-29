n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
n3=int(input("Enter third number"))
if n1>n2 and n1>n3:
    n=n1
elif n2>n3 and n2>n1:
    n=n2
else:
    n=n3
print(f"The biggest number is {n}")
nn=n**2
nnn=n**3
Result=n+nn+nnn
print(f"n+nn+nnn {n}+{nn}+{nnn}={Result}")
radius=n
area=3.14*n**2
perimeter=2*3.14*n
print(f"For Circle with radius {radius}:")
print(f"Area of Circle= {area}")
print(f"Perimeter of Circle= {perimeter}")
print(f"For sphere with radius {radius}:")
volume=(4/3)*(3.14*n**3)
print(f"Volume of sphere= {volume}")

