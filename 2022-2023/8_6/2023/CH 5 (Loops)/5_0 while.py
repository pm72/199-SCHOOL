##print("Programming is fun!\n" * 10)
##
##text = "Programming is fun!\n" * 10
##
##print(text)

'''
while condition:
  ...


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
##s = 0            # 0  1  3  6   10
##while i <= 10:   # 1  2  3  4   5
##  s += i         # 1  3  6  10  15
##  
##  i += 1
##
##print(f"The sum is {s}")
##print(f"Count: {i}")


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

if i % 7 != 0:
  i += (7 - i % 7)

while i <= 324:
  s += i

  print(i, end = '  ')

  i += 7

print(f"\n\nThe sum is {s}")
