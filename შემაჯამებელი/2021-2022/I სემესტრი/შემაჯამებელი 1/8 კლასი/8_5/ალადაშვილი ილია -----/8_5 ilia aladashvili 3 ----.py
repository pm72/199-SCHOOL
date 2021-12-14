Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = random.randint(100,999)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a = random.randint(100,999)
NameError: name 'random' is not defined
seconds = a%60
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    seconds = a%60
NameError: name 'a' is not defined
minutes = int((a - a%60)/60)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    minutes = int((a - a%60)/60)
NameError: name 'a' is not defined
print(a,seconds,minutes)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a,seconds,minutes)
NameError: name 'a' is not defined
