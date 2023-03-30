from time import time

start = time()
for i in range(10**6):
  if i % 2 == 0:
    a = i

print(time() - start)
