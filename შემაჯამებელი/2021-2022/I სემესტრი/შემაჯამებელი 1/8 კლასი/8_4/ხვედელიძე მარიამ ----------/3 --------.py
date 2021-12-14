import random
x=random.randint(100,999)
i=int(0)
j=int(0)
ans1=int(0)
ans2=int(0)
iffound=int(0)
print(x)
while True:
j=0
while True:
if i*60+j==x:
ans1=i
ans2=j
iffound=1;
break
elif i*60+j>x:
break
j += 1
if j==60:
break
i += 1
if iffound==1:
break
print(ans1)
print(ans2)