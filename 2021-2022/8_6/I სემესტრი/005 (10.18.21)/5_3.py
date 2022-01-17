x = int(eval(input("Enter a natural number: ")))    # 0 78654


max_ = 0
while x > 0:
  x1 = x % 10
  if x1 > max_:
    max_ = x1

  x //= 10


print(max_)
