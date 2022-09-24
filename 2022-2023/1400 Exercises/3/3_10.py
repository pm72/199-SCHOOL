k = int(input("Enter amount days [1..365]: "))
d = int(input("Enter weekday [0..6]: "))

n = (d + k) % 7

print(f"Day in week is {n}")
