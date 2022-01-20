# nebismieri ricxvis udidesi cifri


x = int(eval(input("Enter a natural number: ")))     # 5 8 620

min_ = 10
while x > 0:
  x1 = x % 10
  if x1 < min_:
    min_ = x1

  x //= 10


print(min_)
