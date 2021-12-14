mport random
x=random.randint(100,999)
y=int(0)
z=int(0)
ans1=int(0)
ans2=int(0)
j=int(0)
print(x)
while True:
z=0
while True:
if y*60+z==x:
ans1=y
ans2=z
j=1;
break
elif y*60+z>x:
break
z += 1
if z==60:
break
y += 1
if j==1:
break
print(ans1)
print(ans2)
