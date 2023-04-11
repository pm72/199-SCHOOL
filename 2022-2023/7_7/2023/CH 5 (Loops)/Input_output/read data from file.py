file = "data\input.txt"

with open(file=file, mode='r', encoding='utf8') as fin:
  data = fin.read()

data = data.split()

data1 = []
for i in data:
  if not i.isalpha():
    try:
      data1.append(eval(i))
    except SyntaxError:
      num = ''
      for j in i:
        if j.isdigit():
          num += j

      data1.append(eval(num.lstrip('0')))  

avg = sum(data1) / len(data1)

file = "data\output.txt"
data1 = [str(i) for i in data1]
data1 = ' '.join(data1)

with open(file=file, mode='w', encoding='utf8') as fout:
  fout.write(f"{data1}\n\n")
  fout.write(f"საშუალო: {avg:.2f}")


input("\n\nSuccess...\n")
