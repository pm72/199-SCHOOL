a = b = c = -1

while a <= 0 or b <= 0 or c <= 0:
  a, b, c = eval(input("Enter three edges for triangle: "))

if a < b + c and + \
   b < a + c and + \
   c < a + b:
  print(f"The perimeter is {a + b + c}")
else:
  print("The input is invalid")
