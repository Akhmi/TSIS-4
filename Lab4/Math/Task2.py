def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area

base1 = float(input("Enter the length of base1: "))
base2 = float(input("Enter the length of base2: "))
height = float(input("Enter the height: "))

area = trapezoid_area(base1, base2, height)

print("The area of the trapezoid is:", area)
