n = int(input("Enter number of month [1..12]: "))

x = (n + 2 + 11) % 12

print(f"Today's month number is {x}")
