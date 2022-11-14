number1 = 2 / 3
number2 = 15
wd = 15

print(f"{'Number1':<{wd}}{'Number2':<{wd}}{'Free text'}")
print(f"{number1:<{wd}.2f}{number2:<{wd}d}{'One, two, three'}")
print(f"{48.36:<{wd}.2f}{15:<{wd}d}{'One, two, three'}")
print(f"{1.586614:<{wd}.2f}{23:<{wd}d}{'One, two, three'}")

input()
