#6


import random
z=random.randint(10**11,10**12)
k=10
q=0
print(z)
while(z>0):  
      s=z%10
      q=max(s,q)
      k=min(s,k)
      z//=10
      print((q+k)**2)
    
