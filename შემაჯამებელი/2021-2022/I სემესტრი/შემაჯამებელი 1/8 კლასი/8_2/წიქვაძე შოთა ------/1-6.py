#1
#print (((9.5*4.5)-(2.5*3))/(45.5-3.5))

#2
#print((14*5/8)/(45.5)*60)

#3
#import random
#x=random.randint(100,999)
#i=int(0)
#j=int(0)
#ans1=int(0)
#ans2=int(0)
#iffound=int(0)
#print(x)
#while True:
# j=0
# while True:
#
# if i*60+j==x:
# ans1=i
# ans2=j
# iffound=1;
# break
# elif i*60+j>x:
# break
# j += 1
# if j==60:
# break
# i += 1
# if iffound==1:
# break
#print(ans1)
#print(ans2)

#4
#import math
#a=2.59
#b=-8.92
#d=2*b/pow(a,b)
#c=(a-2*b)/pow(d,2)
#r=(2.79*a+3*d)/(pow(b,2)-2*a*c)
#print(4/(3*(r+34))-9*(a+b*c)+(3+d*(2+a))/(a+b*d))

#5
#import math
#a1 = int(input())
#b1 = int(input())
#a2 = int(input())
#b2 = int(input())
#print(math.sqrt(pow(a2-a1,2)+pow(b2-b1,2)))

#6 
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

# ბოდიშით ტელეფონით ვარ და ამიტომ ასე გამოვაგზავნე