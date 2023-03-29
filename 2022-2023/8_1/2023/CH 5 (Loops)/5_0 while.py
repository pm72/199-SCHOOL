'''
while condition:
  ...


[start, stop, step]   [1, 10, 1]
'''

##i = 1
##while i <= 10:
##  print(f"{i}: Programming is fun!")
##
##  i += 1   # 1 = i + 1
##
##print(f"{i}:")


##i = 1
##s = 0            # 0  1  3  6   10  15  21  28  36  45 
##while i <= 10:   # 1  2  3  4   5   6   7   8   9   10
##  s += i         # 1  3  6  10  15  21  28  36  45  55
##
##  i += 1
##  
##print(f"The sum is {s}")


i = 123
s = 0

arr = []

if i % 7 != 0:
  i += (7 - i % 7)

while i <= 324:
  s += i

  print(i, end = '  ')
  arr.append(i)

  i += 7

print(f"\n\nThe sum is {s}")
print(arr)
print(sum(arr))
