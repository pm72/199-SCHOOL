n1 = eval(input("Enter n1: "))
n2 = eval(input("Enter n2: "))

n1, n2 = int(n1), int(n2)

gcd = 1
k = 2

while k <= n1 and k <= n2:
  if n1 % k == 0 and n2 % k == 0:
    gcd = k

  k += 1

print(gcd)
