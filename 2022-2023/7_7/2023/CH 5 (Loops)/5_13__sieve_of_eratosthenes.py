# sieve_of_eratosthenes

N = 2300
A = [True] * N
A[0] = A[1] = False

for i in range(2, N):
  if A[i]:
    for j in range(2 * i, N, i):
      A[j] = False

count = 0
for i in range(N):
  if A[i]:
    count += 1
    print(f"{i:<5d}", end='')

    if count % 5 == 0:
      print()



# ==============
input("\n\nDone!\n")
