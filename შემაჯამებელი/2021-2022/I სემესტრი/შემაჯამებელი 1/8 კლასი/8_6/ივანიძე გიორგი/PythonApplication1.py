#1
print(((9.5*4.5)-(2.5*3))/(45.5 - 3.5))

#2
#ver gavakete

#3
import random
a1=random.randint(100, 1000)
u1=a1//60
s1=a1%60
print(a1)
print(str(u1) + "wuti da" + str(s1) + " wami")

#4 
a2 = 2.59
b2 = -8.92
d2 = (2*b2)/(a2**b2)
c2 = (a2 - 2*b2)/(d2**2)
r2 = (2.79*a2 + 3*d2)/(b2**2 - 2*a2*c2)
print((4/(3*r2+4))-9*(a2+b2*c2)+((3+d2*(2+a2))/(a2+b2*d2)))

#5
import math
x1 = -20
x2 = 11
y1 = 8
y2 = 6
print(math.sqrt((x2-x1)**2 + (y2 - y1)**2))

#6
import random
a3=random.randint(100000000000, 1000000000000)
n3 = 9
x3 = 0
while(a3>0):
    p3=a3%10
    x3=max(p3, x3)
    n3=min(p3, n3)
    a3//= 10
print((x3+n3)**2)
