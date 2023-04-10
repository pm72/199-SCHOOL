with open(file='input.txt', mode='r', encoding='utf8') as fin:
  data = fin.read()


data = [int(i) for i in data.split()]
data = [i for i in data if i > 0]

avg = sum(data) / len(data)

data = [str(i) for i in data]
data = ' '.join(data)

with open(file='output.txt', mode='w', encoding='utf8') as fout:
  fout.write(f"მონაცემები: {data}\n")
  fout.write(f"\nსაშუალო: {avg:.2f}")


input("Success!..")
