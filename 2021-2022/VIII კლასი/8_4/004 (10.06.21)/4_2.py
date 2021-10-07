##x = 83
##print(x % 10 + x // 10)

##
##
##x = 45
##print(x % 10 + x // 10 % 10 + x // 100)


# ----------------

##x = input("Enter a natural number: ")
##s = 0
##for i in range(len(x)):
##  s += int(x[i])
##
##
##print("Sum is", s)


##x = input("Enter a natural number: ")
##s = 0
##for i in x:
##  s += int(i)
##
##print(s)


x = int(eval(input("Enter a natural number: ")))   # 78123
s = 0
if x > 0:
  while x > 0:
    x1 = x % 10
    x = x // 10
    s += x1


print(f"s = {s}")
print(f"x = {x}")
