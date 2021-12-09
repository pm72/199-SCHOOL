##x = 89
##x1 = x % 10
##x2 = x // 10
##
##print(x1 + x2)
##
##
##x = 99
##x1 = x % 10
##x2 = x % 100 // 10  # x2 = x // 10 % 10
##x3 = x // 100
##print(x1 + x2 + x3)



x = input("Enter a integer number: ")
y = 0
for i in range(len(x)):
  y += int((x[i]))


print(y)


y = 0
for i in x:
  y += int(i)

print(y)


s = 0
x = int(x)
while x > 0:
  y = x % 10
  s += y
  x //= 10


print(s)
