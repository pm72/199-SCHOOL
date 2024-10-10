def fibo(arr=[0, 1], maxlen=10):
  if len(arr) == maxlen:
    return arr
  else:
    arr.append(arr[-1] + arr[-2])

    return fibo(maxlen=maxlen)


def fibo2(N):
  arr = []
  a, b = 0, 1

  for _ in range(N):
    arr.append(a)

    a, b = b, a + b
  
  return arr


def fibo_generator(N):
  a, b = 0, 1

  for _ in (range(N)):
    yield a

    a, b = b, a + b


# ===================
n = 10

print(fibo(maxlen=n))
print(fibo2(10))
print(list(fibo_generator(n)))