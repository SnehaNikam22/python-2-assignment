CREATING A FILE NAMES SHAPES

# To find area of the shapes usimg modules
import math
def circle_area(radius):
    return math.pi*radius**2

def rectangle_area(length,bradth):
    return length*bredth

def triangle_area(base,height):
    return 0.5*base*height


NEXT FILE CODE TO IMPORT ABOVE FILE

import shapes
print("choose your shape:")
print("1,for circle")
print("2,for rectangle")
print("3,for triangle")


# Taking the choices input from the user
choices = int(input("Enter your choice of the shapes:"))

# Applying the conditions for the choices
if choices == 1:
    r = float(input("Enter the radius of the circle"))         # for finding area of circle
    area = shapes.circle_area(r)
    print("The area of your circle is:",area)

elif choices == 2:
    l = float(input("Enter the length of the rectangle:"))    # For finding area of rectangle
    b = float(input("Enter the bredth of the rectangle:"))
    area = shapes.rectangle_area(l,b)
    print("The area of the rectangle is:,area")

elif choices == 3:
    base = float(input("Enter the base of the triangle:"))     # for finding area of triangle
    h = float(input("Enter the height of the triangle:"))
    area = shapes.triangle_area(base,h)
    print ("The area of the triangle is:,area")

else
    print("there are no further choices for the shpes")