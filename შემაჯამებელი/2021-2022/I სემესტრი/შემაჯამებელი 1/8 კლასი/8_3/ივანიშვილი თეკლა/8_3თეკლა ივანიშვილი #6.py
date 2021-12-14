import random
x=random.randint(10**11, 10**12)
udidesi=0
umciresi=10
while(x>0):
    y=x%10
    udidesi=max(y,udidesi)
    umciresi=min(y, umciresi)
    x//=10
    print((udidesi+umciresi)**2)
