'''
for i in range(start, stop, step):  for i in range(10):
  ...
  ...
  ...

  
'''

##for i in range(1, 11, 3):
##  print(f"{i}: Programming is fun!..")

##for i in range(10, -1, -1):
##  print(i ** 2)


'''
a, b, h   [0.15, 0.36, 0.015]
'''

a, b, h = 0.15, 0.36, 0.015
s = 0
while a < b:
  s += a
  a += 0.015

print(s)

'''
N = [b - a / h] + 1  int((b - a) / h) + 1
'''
