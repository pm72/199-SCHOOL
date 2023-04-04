'''
while condition:     x < 3:
  ...
  ...
  ...

[start, stop, step]   [1, 10, 1]
  

'''
##
##print("Programming is fun!\n" * 10)
##
##text = "Programming is fun!\n" * 10
##
##print(text)

##i = 1
##while i <= 10:
##  print(f"{i}: Programming is fun!")
##  
##  i += 1  # i = i + 1
##
##print(f"{i}: ")


##i = 1
##s = 0            # 0  1   3   6   10  15  21  28  36  45
##while i <= 10:   # 1  2   3   4   5   6   7   8   9   10
##  s += i         # 1  3   6   10  15  21  28  36  45  55
##
##  i += 1
##
##print(s)


i = 123
s = 0
d = 47

if i % d != 0:
  i += (d - i % d)    # 47 - i % 47

while i <= 324:
  s += i
  print(i, end='  ')
  i += d

print("\n\n", s)
