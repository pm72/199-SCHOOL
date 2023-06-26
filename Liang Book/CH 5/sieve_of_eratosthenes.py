N = int(eval(input("Amount items in list: ")))
A = [True] * N
A[0] = A[1] = False

for i in range(2, N):
  if A[i]:
    for j in range(2 * i, N, i):
      A[j] = False

##for i in range(N):
##  print(i, '–', 'is Prime' if A[i] else "isn't prime")

print(f"The prime numbers are:\n")
count = 0
for i in range(2, N):
  if A[i]:
    count += 1
    print(f"{i:<5d}", end='')

    if count % 10 == 0:
      print()
