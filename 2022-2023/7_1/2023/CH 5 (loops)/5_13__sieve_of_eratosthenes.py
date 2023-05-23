N = 50
A = [True] * N
A[0] = A[1] = False

for i in range(2, N):
  if A[i]:
    for j in range(2*i, N, i):
      A[j] = False

for i in range(N):
  if A[i]:
    print(f"{i:<5d}", end='')


# ============
input("\n\nDone\n")
