##x = 76
##x1 = x % 10
##x2 = x // 10
##
##print(x1 + x2, "\n")
##
##
##x = 789
##x1 = x % 10
##x2 = x // 10 % 10
##x3 = x // 100
##
##print(x1 + x2 + x3, "\n")


num = input("Enter a natural number: ")
s = 0
for i in range(len(num)):
  s += int(num[i])

print(s)



s = 0
for i in num:
  s += int(i)

print(s)
