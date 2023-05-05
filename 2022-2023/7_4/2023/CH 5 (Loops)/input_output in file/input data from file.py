file = 'input.txt'

with open(file=file, mode='r', encoding='utf8') as fin:
  data = fin.read()

data = data.split()
data1 = []

for i in data:
  try:
    if type(eval(i)) != bool: 
      data1.append(eval(i))
  except (NameError, SyntaxError):
    num = ''
    for j in i:
      if j.isdigit():
        num += j

    if num:
      data1.append(eval(num.lstrip('0')))

avg = sum(data1) / len(data1)

print(*data1)
print(f"\n\nThe average is {avg:.2f}")
