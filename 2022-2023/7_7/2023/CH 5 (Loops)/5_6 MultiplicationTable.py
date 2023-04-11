print(' ' * 6, end='')
for i in range(1, 10):
  print(f"{i:<4d}", end='')

print()
print('-' * 42)

for i in range(1, 10):
  print(f"{i}{' |':<5s}", end='')

  for j in range(1, 10):
    print(f"{(i * j):<4d}", end='')

  print()
    
