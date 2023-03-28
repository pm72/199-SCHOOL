##print("Programming is fun!\n" * 10)
##
##i = 1
##while i <= 10:
##  print("5_0 while.py")
##
##  i += 1


##i = 1
##s = 0            # s = 0
##while i <= 10:   # i = 1  2  3  4   5   6   7   8   9   10
##  s = s + i      # s = 1  3  6  10  15  21  28  36  45  55
##
##  i += 1
##
##print(f"The sum of 1 and {i - 1} numbers is {s}")


##i = 97
##j = 158
##s = 0
##print(f"The sum of {i}", end=' ')   # The sum of {i} 
##while i <= j:
##  s = s + i
##
##  i += 1
##
##print(f"and {j} numbers is {s}")



i = 1
j = 10
s = 0

even_odd = "odd"
if i % 2 == 1:
  i += 1
  even_odd = "even"

print(f"The sum of {i}", end=' ')   # The sum of {i}

while i <= j:
  s = s + i

i += 2

print(f"and {j} {even_odd} numbers is {s}")
