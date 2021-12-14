Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

print(((9.5*4.5)-(2.5*3))/(45.5 - 3.5))


kms = 14.0
miles = kms/1.6
minutes = 45.5
miles_in_1_minute = miles/minutes
miles_in_1_hour = miles_in_1_minute * 60
print(str(miles_in_1_hour) + " miles/hour")

import random
a = random.randint(100, 1000)
minutes = a//60
seconds = a%60
print(str(minutes) + " minutes and " + str(seconds) + " seconds")

a = 2.59
b = -8.92
d = (2*b)/(a**b)
c = (a - 2*b)/(d**2)
r = (2.79*a + 3*d)/(b**2 - 2*a*c)
print((4/(3*r+4))-9*(a+b*c)+((3+d*(2+a))/(a+b*d)))

x1 = -20
x2 = 11
y1 = 8
y2 = 6
print(math.sqrt((x2-x1)**2 + (y2 - y1)**2))

import random
a = random.randint(10**11, 10**12)
mn = 10
mx = 0
while (a>0):
    k = a%10
    mx = max(k, mx)
    mn = min(k, mn)
    a //= 10
print((mx+mn)**2)


SyntaxError: multiple statements found while compiling a single statement