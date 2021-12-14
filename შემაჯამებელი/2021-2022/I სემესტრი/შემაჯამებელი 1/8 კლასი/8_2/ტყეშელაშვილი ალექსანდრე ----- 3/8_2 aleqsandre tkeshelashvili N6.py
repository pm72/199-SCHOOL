Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
a = random.randint(10**11, 10**12)
mn = 10
mx = 0
while (a>0):
    k = a%10
    mx = max(k, mx)
    mn = min(k, mn)
    a //= 10
print((mx+mn)**2