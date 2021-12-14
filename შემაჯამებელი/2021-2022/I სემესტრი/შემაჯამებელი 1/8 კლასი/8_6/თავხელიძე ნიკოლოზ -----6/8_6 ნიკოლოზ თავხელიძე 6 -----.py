import random as r
a=r.randint(1, 10**12 - 1)
mn=9
mx=0
print(a)
while a:  # while a!= 0, while a!= ''
	if a % 10 < mn:
		mn = a % 10
	elif a % 10 > mx:
		mx = a % 10
	
	a //= 10

print(mn, mx)
print((mx+mn)**2)


input()