##print("Programming is fun!\n" * 10)
##
##text = "Programming is fun!\n" * 10
##
##print(text)


'''
while condition:
  ...

print("Programming is fun!")

[start, stop, step]   [1, 10, 1]

'''

##i = 1
##while i <= 10:
##  print(f"{i}: Programming is fun!")
##
##  i += 1   # i = i + 1
##
##print(f"{i}: ")


##i = 1
##s = 0            # 0  1  3  6   10  15  21  28  36  45
##while i <= 10:   # 1  2  3  4   5   6   7   8   9   10
##  s += i         # 1  3  6  10  15  21  28  36  45  55
##
##  i += 1
##
##print(f"The sum is {s}")



##i = 123
##s = 0
##
##if i % 2 == 1:
##  i += 1
##
##while i <= 324:
##  s += i
##
##  i += 2
##
##print(f"The sum is {s}")


i = 123
s = 0

while i % 17 != 0:
  i += 1

while i <= 324:
  s += i

  print(i, end='  ')
  
  i += 17

print(f"\nThe sum is {s}")
