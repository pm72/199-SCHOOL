##for i in range(10, 0, -1):   # [a, b-1, step)
##  print(i, end=' ')


##a = [15, 2.56, "Paata", True, -89, (58, 15, 25, "False")]
##for i in a:
####  if type(i) == int or type(i) == float:
##    print(i)
##
##print(type(a[-1]))


with open(file="data\input.txt", mode='r', encoding='utf8') as fin:
  data = fin.read()

data = data.split()
data = [int(i) for i in data]

avg = sum(data) / len(data)

data = [str(i) for i in data]
data = ' '.join(data)

with open(file="data\output.txt", mode='w', encoding='utf8') as fout:
  fout.write(f"ქულები:\n{data}\n\n")
  fout.write(f"საშუალო: {avg:.2f}")
