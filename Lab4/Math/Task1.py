import math

def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians

degrees = float(input("Enter the degree value: "))

radians = degrees_to_radians(degrees)

print("Radians:", radians)
