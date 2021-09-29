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
  y += int(x[i])


print(y)
