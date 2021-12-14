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
a = random.randint(100, 1000)
minutes = a//60
seconds = a%60
print(str(minutes) + " minutes and " + str(seconds) + " seconds")

#4 
k = 2.59
l = -8.92
t = (2*l)/(k**l)
m = (k - 2*l)/(t**2)
n = (2.79*k + 3*t)/(l**2 - 2*k*m)
print((4/(3*n+4))-9*(k+l*m)+((3+t*(2+k))/(k+l*t)))

#5
import math
x1 = -20
x2 = 11
y1 = 8
y2 = 6
print(math.sqrt((x2-x1)**2 + (y2 - y1)**2))

#6 
o = 12.512 - 3.98j
i = a.real
l = a.imag
print((i+l)/2)
