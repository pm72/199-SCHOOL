def outer(N):
  a, b = 0, 1

  def fibo():
    nonlocal a, b

    for _ in range(N):
      yield a

      a, b = b, a + b
  
  yield fibo


def outer2(N):
  a, b, arr = 0, 1, []

  def fibo():
    nonlocal a, b

    for _ in range(N):
      arr.append(a)

      a, b = b, a + b
    
    return arr
  
  return fibo


# ===============
num = 10

for i in outer(num):
  print(*i())

print(* outer2(num)())

# for i in outer2(num)():
#   print(i, end=' ')

# print()