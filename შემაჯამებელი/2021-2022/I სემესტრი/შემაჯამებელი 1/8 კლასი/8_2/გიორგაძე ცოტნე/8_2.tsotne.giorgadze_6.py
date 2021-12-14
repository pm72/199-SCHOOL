from random import randint

num=randint(100000000000, 999999999999)
num=str(num)
ans=max([int(i) for i in num])+min([int(i) for i in num])

print(ans**2)


input()