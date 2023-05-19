A = range(1, 89, 3)

count = 0
for i in A:
  count += 1

  print(f"{i:<5d}", end='')

  if count % 3 == 0:
    print()
