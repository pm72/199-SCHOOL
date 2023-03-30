##print("Programming is fun!\n" * 10)
##
##text = "Programming is fun!\n" * 10
##
##print(text)


'''
while condition:    x < 5:
  ...
  ...
  ...

[start, stop, step]  [1, 10, 1]
  
'''

##i = 1
##while i <= 10:
##  print(f"{i}: Programming is fun!")
##
##  if i == 5:
##    break
##
##  i += 1  # i = i + 1
##else:
##  print(f"{i}: ")
##
##print("Witout else", i)
##


##i = 1
##s = 0           # 0  1  3  6   10
##while i <= 10:  # 1  2  3  4   5   6  7  8  9  10
##  s += i        # 1  3  6  10  15
##
##  i += 1
##
##print(s)


i = 123
s = 0
d = 18

if i % d != 0:
  i += d - (i % d)

while i <= 324:
  s += i

  print(i, end='  ')

  i += d

print(f"\n\n{s}")
