##x = 99
##print(x % 10 + x // 10)



##x = input("Enter a natural number: ")
##s = 0

##for i in range(len(x)):
##  s += int(x[i])

##for i in x:
##  s += int(i)


x = int(eval(input("Enter a natural number: ")))
s = 0
while x > 0:
  s += x % 10
  x //= 10



print(s)
