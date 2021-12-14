from random import randint

a=randint(100000000000, 999999999999)
a=str(a)
b=max([int(j) for j in num])+min([int(j) for j in a])
print(b**2)


input()