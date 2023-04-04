s = 0
i = 1
N = 5

while i <= N:
  data = eval(input("Enter a number: "))

  s += data

  i += 1

print(f"The average: {(s / N):.2f}")
