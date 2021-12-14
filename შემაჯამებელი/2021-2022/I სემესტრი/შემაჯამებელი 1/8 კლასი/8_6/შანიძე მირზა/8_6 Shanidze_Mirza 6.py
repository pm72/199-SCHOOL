import random
a = random.randint(pow(10, 11), pow(10, 12))
umciresi = 10 
udidesi = 0
while (a>0):
    p = a%10
    udidesi = max(p, udidesi)
    umciresi = min(p, umciresi)
    a //= 10
print((umciresi+udidesi)**2)


