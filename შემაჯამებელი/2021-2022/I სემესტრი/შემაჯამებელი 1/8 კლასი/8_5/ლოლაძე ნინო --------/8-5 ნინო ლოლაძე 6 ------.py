import random
a = random.randint(12**11,12**12)
mn = 12
mx = 0
while(a>0):
  k=a%12
  mx = max(k, mx)
  mn = min (k,mn)
  a//=12
print((mx+mn)**2)
