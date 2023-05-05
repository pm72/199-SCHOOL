n1 = int(eval(input("Enter n1: ")))
n2 = int(eval(input("Enter n2: ")))

k = 2
gcd = 1

while k <= min(n1, n2):
  if n1 % k == 0 and n2 % k == 0:
    gcd = k

  k += 1

print(gcd)
