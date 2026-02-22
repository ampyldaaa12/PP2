import math

n_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))
# Area = (n * a^2) / (4 * tan(pi/n))
polygon_area = (n_sides * side_length**2) / (4 * math.tan(math.pi / n_sides))
print(f"The area of the polygon is: {polygon_area}\n")