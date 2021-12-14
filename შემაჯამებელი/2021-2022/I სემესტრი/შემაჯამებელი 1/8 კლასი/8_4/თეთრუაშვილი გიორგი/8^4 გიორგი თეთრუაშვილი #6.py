import random
a = random.randint(100000000000,999999999999)
t=str(a)
b=0
s=10000000000000
for n in range(0,11):
    if int(t[n])>b:
        b=int(t[n])

    if int(t[n]) < s:
        s = int(t[n])

print((b+s)**2)
