##print("Programming is fun!\n" * 10)
##
##test = "Programming is fun!\n" * 10


'''
while condition:   x < 8:
  ...
  ...
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
##m = 1
##s = 0            # 0  1  3  6   10  15
##while i <= 10:   # 1  2  3  4   5   6  ...
##  s += i         # 1  3  6  10  15  21
##  m *= i
##
##  i += 1
##
##print(f"The sum is {s}")
##
##
##print(sum(range(1, 11)))



i = 123
s = 0
d = 17

while i % d != 0:
  i += 1

while i <= 324:
  s += i

  print(i, end='  ')

  i += d

print(f"\n\n{s}")
