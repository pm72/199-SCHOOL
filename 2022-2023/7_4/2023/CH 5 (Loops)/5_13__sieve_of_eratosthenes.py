N = 230
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
        print(f"{i: <6d}", end='')
        
        if count % 10 == 0:
            print()

print(f"\n\nCount: {count}")
