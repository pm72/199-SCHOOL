##x = int(input("Enter a natural number: "))   # 8562
##
##s = 0
##temp = x
##while temp > 0:
##  s += temp % 10
##  temp //= 10
##
##
##print(s)
##print(x)
##
##
##
##s = 1
##temp = x
##while temp > 0:
##  s *= temp % 10
##  temp //= 10
##
##print(s)
##print(x)


x1 = 58
x2 = 21

if x1 > x2:
  print(f"{x1} > {x2}")
elif x2 > x1:
  print(f"{x2} > {x1}")
else:
  print(f"{x1} = {x2}")
