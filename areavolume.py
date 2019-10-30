import math

def areaCircle():
    pi = math.pi
    r = float(input("Input the radius of the circle : "))
    area = pi * r * r
    print ("Area of the circle is : %.2f" %area)

areaCircle()

def areaSquare():
    s = float(input("Input one side of the square : "))
    area = s * s
    print("Area of the square is : %.2f" %area)

areaSquare()

def volumeSphere():
    pi =  math.pi
    r = float(input("Input the radius of the sphere : "))
    volume = 4/3 * pi * r ** 3
    print("Volume of the sphere is : %.2f " %volume)

volumeSphere()

def volumeCylinder():
    pi = math.pi
    r = float(input("Input the radius of the cylinder : "))
    h = float(input("Input the height of the cylinder : "))
    volume = pi * r * r * h
    print("Volume of the cylinder is : %.2f " %volume)

volumeCylinder()