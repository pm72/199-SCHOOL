#1
print(((9.5*4.5)-(2.5*3))/(45.5 - 3.5))

#2
kms = 14.0
miles = kms/1.6
minutes = 45.5
miles_in_1_minute = miles/minutes
miles_in_1_hour = miles_in_1_minute * 60
print(str(miles_in_1_hour) + " miles/hour")

#3
import random
f = random.randint(100, 1000)
minutes = f//60
seconds = f%60
print(str(minutes) + " minutes and " + str(seconds) + " seconds")

#4 
a = 2.59
b = -8.92
d = (2*b)/(a**b)
c = (a - 2*b)/(d**2)
k = (2.79*a + 3*d)/(b**2 - 2*a*c)
print((4/(3*k+4))-9*(a+b*c)+((3+d*(2+a))/(a+b*d)))

#5
import math
x1 = -20
x2 = 11
y1 = 8
y2 = 6
print(math.sqrt((x2-x1)**2 + (y2 - y1)**2))

#6 
j = 12.512 - 3.98j
m = a.real
n = a.imag
print((m+n)/2)
