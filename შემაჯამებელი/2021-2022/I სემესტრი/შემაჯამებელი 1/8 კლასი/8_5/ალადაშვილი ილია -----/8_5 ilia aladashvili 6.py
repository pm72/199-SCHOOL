Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
a = random.randint(10**11,10**12)
mn = 10
mx = 0
while(a>0):
   k = a%10
   mx = max(k,mx)
   mn = min(k,mm)
   m//= 10
print((mx+mn)**2)
SyntaxError: invalid syntax
