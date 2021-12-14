import random as ana
num = ana.randint(100000000000, 999999999999)
ab = 10
ac = 0
while num>0:
    x = num%10
    ac = max(x, ac)
    ab = min(x, ab)
    num //= 10
print((ab+ac)**2)


