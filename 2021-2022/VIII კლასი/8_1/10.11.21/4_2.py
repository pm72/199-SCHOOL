x = int(eval(input("Enter a natural number: ")))     # 8562


s = 0
while x:         # while x > 0
  s = s + x % 10
  x = x // 10

print(s)
