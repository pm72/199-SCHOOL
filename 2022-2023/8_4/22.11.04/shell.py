Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#  2_14
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4

a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

p = (a + b+ c) / 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("The area of the triangle is", round(s, 2))
The area of the triangle is 33.6


# 2_12
text = "a    b   a ** b\n"
text += "1    2    1\n"
n"
text += "2    3    8\n"
SyntaxError: unterminated string literal (detected at line 1)
text += "1    2    1\n"
text += "3    4    81\n"
text += "4    5    1024\n"
text += "5    6    15625\n"

text
'a    b   a ** b\n1    2    1\n1    2    1\n3    4    81\n4    5    1024\n5    6    15625\n'

print(text)
a    b   a ** b
1    2    1
1    2    1
3    4    81
4    5    1024
5    6    15625


================= RESTART: D:/199/8_4/22.11.04/2_12.py =================
a    b   a ** b
1    2    1
3    4    81
4    5    1024
5    6    15625

================= RESTART: D:/199/8_4/22.11.04/2_12.py =================
a    b    a ** b
1    2    1
3    4    81
4    5    1024
5    6    15625
"3    4    81
SyntaxError: unterminated string literal (detected at line 1)



# 2_13
x = 3125
print(x % 10, x // 10 % 10, x // 100, % 10, x // 1000 sep='')
SyntaxError: invalid syntax
print(x % 10, x // 10 % 10, x // 100 % 10, x // 1000 sep='')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(x % 10, x // 10 % 10, x // 100 % 10, x // 1000, sep='')
5213



def func(x):
    reverse_x = 0

    

def func(x):
    reverse_x = 0
    while(x):
        revers_x = reverse_x * 10 + x % 10

        

def func(x):
    reverse_x = 0
    while(x):
        revers_x = reverse_x * 10 + x % 10
    return reverse_x

func(7500)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    func(7500)
  File "<pyshell#49>", line 3, in func
    while(x):
KeyboardInterrupt

print(func(7500))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(func(7500))
  File "<pyshell#49>", line 3, in func
    while(x):
KeyboardInterrupt


================= RESTART: D:/199/8_4/22.11.04/2_12.py =================
Enter number: 7500
57

================= RESTART: D:/199/8_4/22.11.04/2_12.py =================
Enter number: 1587456230354
4530326547851



x = 500
x1 = x % 60
x2 = x // 60
x3 = x // 3600
print(x3, x2, x1, sep=':')
0:8:20
0*3600 + 8*60 + 20
500

x = 5000
x1 = x % 60
x2 = x // 60 % 60
x3 = x // 3600
print(x3, x2, x1, sep=':')
1:23:20
1*3600 + 23*60 + 20
5000

x = 138574
x1 = x % 60
x2 = x // 60 % 60
x3 = x // 3600 % 24
print(x3, x2, x1, sep=':')
14:29:34
38*3600 + 29*60 + 34
138574



import time
time.time()
1667557704.0366874
time.time()
1667557718.5139635
time.time()
1667557720.8262932
time.time()
1667557722.5195477


>>> from time import time as t
>>> int(t())
1667557768
>>> int(t())
1667557772
>>> int(t())
1667557774
>>> int(t())
1667557777
>>> int(t())
1667557780
>>> 
>>> print(int(t()) // 3600 % 24, int(t()) // 60 % 60, int(t()) % 60, sep=':')
10:31:1
>>> print(int(t()) // 3600 % 24, int(t()) // 60 % 60, int(t()) % 60, sep=':')
10:31:16
>>> print(int(t()) // 3600 % 24, int(t()) // 60 % 60, int(t()) % 60, sep=':')
10:31:27
>>> print(int(t()) // 3600 % 24 + 4, int(t()) // 60 % 60, int(t()) % 60, sep=':')
14:32:7
>>> 
>>> print((int(t()) // 3600 % 24 + 4) % 24, int(t()) // 60 % 60, int(t()) % 60, sep=':')
14:34:0
