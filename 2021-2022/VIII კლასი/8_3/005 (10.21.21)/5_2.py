x = int(input("Enter a natural number: "))   # 0  8   7     5 6 3 2 0

max_ = x % 10
x //= 10

while x > 0:
  x1 = x % 10
  if x1 > max_:
    max_ = x1

  x //= 10

print(max_)
