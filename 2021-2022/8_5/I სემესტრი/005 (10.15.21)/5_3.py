x = int(eval(input("Enter a natural number: ")))   # 685721

max_ = 0
while x > 0:
  x1 = x % 10
  if x1 > max_:
    max_ = x1
  
  x //= 10

print(max_)
