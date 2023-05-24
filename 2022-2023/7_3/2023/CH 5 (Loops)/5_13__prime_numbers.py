#!/usr/bin/env python
# coding: utf-8

# # პირველი N მარტივი რიცხვი

# In[21]:


N = 50
number = 2
count = 0

while count < N:
    divisor = 2
    
    while divisor <= number ** 0.5:
        if number % divisor == 0:
            break
        
        divisor += 1
    
    else:
        count += 1
        print(f"{number:<6d}", end='')
        
        if count % 10 == 0:
            print()
    
    number += 1

print("\n\n", count)


# # მარტივი მამრავლები

# In[28]:


number = int(eval(input("Enter a number: ")))
divisor = 2

while number > 1:
    if number % divisor == 0:
        print(f"{divisor:<5d}", end='')
        number //= divisor
    else:
        divisor += 1

# 20  10  5  1
# 2   2   5


# # ერასტოფენეს საცერი

# In[41]:


N = 50
A = [True] * N
A[0] = A[1] = False

for i in range(2, N):
    if A[i]:
        for j in range(2 * i, N, i):
           A[j] = False

count = 0
for i in range(2, N):
    if A[i]:
        count += 1
        print(f"{i:<6d}", end='')
        
        if count % 10 == 0:
            print()

print(f"\n\nCount: {count}")


# In[ ]:




