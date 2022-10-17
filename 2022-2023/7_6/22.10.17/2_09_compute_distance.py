# Enter the first point with two float values
x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))  # 2.59, 1.25

# Enter the second point with two float values
x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))

# Compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print("The distance between the two points is", round(distance, 2))
