Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 2_13
x = 5843
print(x % 10, x // 10 % 10, x // 100 % 10, x // 1000)
3 4 8 5
print(x % 10, x // 10 % 10, x // 100 % 10, x // 1000, sep='')
3485
3485
3485




# 2_14
2 ** (1/2)
1.4142135623730951
2 ** (1/3)
1.2599210498948732
2 ** (2/3)
1.5874010519681994
2 ** (3/3)
2.0
2 ** (4/3)
2.5198420997897464



x = 500
x1 = x % 60
x2 = x // 60
x3 = x // 3600
print(x3, x2, x1, sep=':')
0:8:20

x = 5000
x1 = x % 60
x2 = x // 60 % 60
x3 = x // 3600
print(x3, x2, x1, sep=':')
1:23:20
1*3600 + 23*60 + 20
5000


x = 138456
x1 = x % 60
x2 = x // 60 % 60
x3 = x // 3600 % 24
print(x3, x2, x1, sep=':')
14:27:36
83*3600 + 27*60 + 36
300456
38*3600 + 27*60 + 36
138456



import time as t
t.time()
1667551252.7419305
t.time()1667551252.7419305
SyntaxError: invalid syntax


t.time()1667551252.7419305
SyntaxError: invalid syntax
t.time()
1667551288.645597
t.time()
1667551291.145386
t.time()
1667551298.5042295
t.time()
1667551302.6445904

int(t.time())
1667551375
int(t.time())
1667551378
int(t.time())
1667551379
int(t.time())
1667551380



from time import time as t
t()
1667551404.1841605


print(int(t) // 3600 % 24, int(t) // 60 % 60, int(t) % 60)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print(int(t) // 3600 % 24, int(t) // 60 % 60, int(t) % 60)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'builtin_function_or_method'
>>> 
>>> 
>>> print(int(t()) // 3600 % 24, int(t()) // 60 % 60, int(t()) % 60)
8 45 22
>>> print(int(t()) // 3600 % 24, int(t()) // 60 % 60, int(t()) % 60, sep=":")
8:45:34
>>> 
>>> print(int(t()) // 3600 % 24 + 4, int(t()) // 60 % 60, int(t()) % 60, sep=":")
12:46:28
>>> print((int(t()) // 3600 % 24 + 4) % 24, int(t()) // 60 % 60, int(t()) % 60, sep=":")
12:48:19
>>> print((int(t()) // 3600 % 24-7) % 24, int(t()) // 60 % 60, int(t()) % 60, sep=":")
1:49:20
>>> print((int(t()) // 3600 % 24 + 4) % 24, int(t()) // 60 % 60, int(t()) % 60, sep=":")
12:49:52
>>> 
>>> 
>>> 
