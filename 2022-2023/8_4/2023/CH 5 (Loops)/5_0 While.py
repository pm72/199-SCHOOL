'''

while condition:    x < 3:
  ...
  ...
  ...


  [start, stop, step]    [1, 10, 1]

'''

##print("Programming is fun!..\n" * 10)
##
##text = "Programming is fun!..\n" * 10
##
##print(text)

##i = 1
##while i <= 10:
##  print(f"{i}: Programming is fun!..")
##
##  i += 1   # i = i + 1
##
##print(f"{i}: ")



i = 123
s = 0
d = 7

i += (d - i % d)

while i <= 324:
  s += i
  print(i, end='  ')
  i += d

print("\n\n",s)
