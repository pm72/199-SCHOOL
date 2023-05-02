n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
k = 2
gcd = 1

while k <= n1 and k <= n2:
  if n1 % k == 0 and n2 % k == 0:
    gcd = k

  k += 1

print(gcd)
