x = int(eval(input("Enter a natural number: ")))    # 0  7856240

max_ = x % 10
x //= 10

while x > 0:
  if x % 10 > max_:
    max_ = x % 10

  x //= 10


print(max_)
  
