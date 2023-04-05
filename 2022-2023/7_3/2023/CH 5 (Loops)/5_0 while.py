##print("Programming is fun!\n" * 10)
##
##i = 1
##while i <= 10:
##  print(f"{i}: Programming is fun!")
##
##  i += 1  # i = i + 1
##
##print(i)


# [1, 10, 1]  [start, stop, step]

##i = 2
##jami = 1
##namravli = 1
##while i <= 10:    # 1  2  3  4   5   6   7   8   9   10
##  jami += i       # 1  3  6  10  15  21  28  36  45  55
##  namravli *= i
##  
##  i += 1
##
##print(f"The sum is {jami}")
##print(f"The multiply is {namravli}")


i = 123
s = 0
d = 2

if i % d != 0:
  i += (d - i % d)

while i <= 324:
  s += i
  print(i, end='  ')
  i += d

print(f"\n\nThe sum is {s}")
