file = "input_data.txt"
print(file)
with open(file=file, mode='r', encoding='utf8') as fin:
  data = fin.read()
