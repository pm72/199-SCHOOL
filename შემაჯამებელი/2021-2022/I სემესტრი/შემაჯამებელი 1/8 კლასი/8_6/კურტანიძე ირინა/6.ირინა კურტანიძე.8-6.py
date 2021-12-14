Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
r = random.randint(10**11, 10**12)
a = 10
b = 0
while (r>0):
    x = r%10
    b = max(x, b)
    a = min(x, a)
    r //= 10
print((b+a)**2)