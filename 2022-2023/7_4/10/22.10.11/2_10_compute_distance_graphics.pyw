import turtle as t

t.setup(800, 600)
t.title("Copmute Distance Graphics")

# Prompt the user for inputting two points
x1 = t.numinput("Coordinates for Point 1", "x1 for point 1")
y1 = t.numinput("Coordinates for Point 1", "y1 for point 1")

x2 = t.numinput("Coordinates for Point 2", "x2 for point 2")
y2 = t.numinput("Coordinates for Point 2", "y2 for point 2")

# Compute the distance
distance = ((x1 - x2) **2 + (y1 - y2) ** 2) ** 0.5

# Display two points and the connecting line
t.penup()
t.goto(x1, y1)  # Move to (x1, y1)
t.pendown()
t.write(f"Point 1 ({x1}, {y1})", font=('calibri', 14))

t.goto(x2, y2)  # Draw a line to (x2, y2)
t.write(f"Point 2 ({y1}, {y2})", font=('calibri', 14))

# Move to the center point of the line
t.penup()
t.goto((x1 + x2) / 2, (y1 + y2) / 2)
t.pendown()
t.write(f"The distance between two points is {round(distance, 2)}",
        font=("calibri", 14))

t.exitonclick()  # pause
