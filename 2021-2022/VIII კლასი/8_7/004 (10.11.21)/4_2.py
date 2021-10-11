x = int(input("Enter a natural number: "))         # 8562


s = 0
while x:
  s = s + x % 10
  x = x // 10

print(s)
