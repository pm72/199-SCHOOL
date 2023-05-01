from sys import argv

with open(file="input.txt", mode='r', encoding='utf8') as fin:
  data = fin.read()

data = data.split()
data = [int(i) for i in data]
data = [i for i in data if i > 0]

avg = sum(data) / len(data)

##data = [str(i) for i in data]

##data = ' '.join(data)

##file = argv[1] + " " + argv[2] + ".txt"
file = "Output.txt"

with open(file=file, mode='w', encoding='utf8') as fout:
  fout.write("ქულები:\n" + ' '.join(f"{i}" for i in data) + "\n\n")
  fout.write(f"საშუალო: {avg:.2f}")


input("Success!..")
