from graphics import rectangle
a=int(input("enter the length of rectangle:"))
b=int(input("enter the breath of rectangle:"))
area=rectangle.area_rectangle(a,b)
perimeter=rectangle.perimeter(a,b)

from graphics import circle
r=int(input("enter radious of the circle:"))
ar=circle.area_circle(r)
pr=circle.perimeter_circle(r)

from graphics.graphics_3d import sphare
radius=int(input("enter radious of the sphare:"))
sar=sphare.spare(radius)
perimeter_sphare=sphare.perimeter(radius)

from graphics.graphics_3d import cuboid
h=int(input("enter the hight of the cuboid:"))
l=int(input("enter the length of the cuboid:"))
b=int(input("enter the breadth of the cuboid:"))
area_cuboid=cuboid.area_cuboid(l,b,h)
perimeter_cuboid=cuboid.cuboid_perimeter(l,b,h)