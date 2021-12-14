Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:\Users\pc\Desktop\shemajamebeli.py ================
0.8392857142857143
11.538461538461538m/t
5 wuti da 41 wami
-23.82497621517337
31.064449134018133
Traceback (most recent call last):
  File "C:\Users\pc\Desktop\shemajamebeli.py", line 43, in <module>
    big= min(k, lilaha)
NameError: name 'lilaha' is not defined
>>> rint(((9.5*4.5)-(2.5*3))/(45.5 - 3.5))


v=14
t=45.5 #wutebshi
m=v/1.6
print(str((m/t)*60) + "m/t")


import random
a = random.randint(100, 1000)
mint=a//60
sec=a%60
print(str(mint) + " wuti da " + str(sec) + " wami")


a = 2.59
b = -8.92
d = (2*b)/(a**b)
c = (a - 2*b)/(d**2)
r = (2.79*a + 3*d)/(b**2 - 2*a*c)
print((4/(4+3*r))-9*(a+b*c)+((3+d*(2+a))/(a+b*d)))




import math
a = -20
b = 11
c = 8
d = 6
print(math.sqrt((b-a)**2 + (c - d)**2))



import random
a = random.randint(10**11, 10**12)
lit = 10
big= 0
while (a>0):
    k = a%10
    lit= max(k, big)
    big= min(k, lilaha)
    a //= 10
print((big+lil)**2)
