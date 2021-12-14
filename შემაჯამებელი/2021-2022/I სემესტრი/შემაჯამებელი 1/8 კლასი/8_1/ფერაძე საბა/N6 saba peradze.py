import random
x = random.randint(10**11 , 10**12)
minnumber = 11
maxnumber = 0


print(x)
while (x>0):

    nm = x % 10
    maxnumber = max(nm,maxnumber)
    minnumber = min(nm, minnumber)
    x = x//10


print((maxnumber+minnumber)**2)
