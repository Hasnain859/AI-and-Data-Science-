import math

def compute_circle_area_circumference(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference
area, circumference = compute_circle_area_circumference(5)
print("Area:", area)
print("Circumference:", circumference)
