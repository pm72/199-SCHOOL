x = int(input("Enter a natural number: "))    # 8562

##print(sum(int(i) for i in x))

s = 0

while x > 0:          # 2
  s += x % 10         # s = s + (x % 10)    2
  x //= 10            # 856    85  8                8   13  21

print(s)
