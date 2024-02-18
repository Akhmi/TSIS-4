import math

def regular_polygon_area(n, s):
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    return area

n = int(input("Enter the number of sides: "))
s = float(input("Enter the length of one side: "))

area = regular_polygon_area(n, s)

print("The area of the regular polygon is:", area)