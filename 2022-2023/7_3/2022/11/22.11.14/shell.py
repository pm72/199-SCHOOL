Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ord("1")
49
ord("A")
65
ord('1', 'A')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ord('1', 'A')
TypeError: ord() takes exactly one argument (2 given)


ord('B')
66
ord('a')
97
ord('b')
98

chr(40)
'('
chr(59)
';'
chr(79)
'O'
chr(85)
'U'
chr(90)
'Z'
chr(91)
'['


print(""")
"


KeyboardInterrupt

print("\"")
"
print("\'")
'
print("\\")
\


print("He said, "John's program is easy to read"")
SyntaxError: unterminated string literal (detected at line 1)

print("He said, \"John's program is easy to read"")
SyntaxError: unterminated string literal (detected at line 1)

print("He said, \"John's program is easy to read\"")
He said, "John's program is easy to read"

print('He said, "John\'s program is easy to read')
He said, "John's program is easy to read

print("He said, 'John\'s program is easy to read'")
He said, 'John's program is easy to read'


print("D:\199\7_3\22.11.07\shell.py")
D:99_3.11.07\shell.py

print("D:\\199\\7_3\\22.11.07\\shell.py")
D:\199\7_3\22.11.07\shell.py

print("D:\kile\shell.py")
D:\kile\shell.py
print("D:
ile\shell.py")
SyntaxError: unterminated string literal (detected at line 1)
print("D:\nile\shell.py")
D:
ile\shell.py

print("D:\nile\bell.py")
D:
ileell.py
print("D:\\nile\\bell.py")
D:\nile\bell.py


print('\\"')
\"
print("\\ \"")
\ "

print('\u03b1')
α


x = input("Enter a character: ")
ch = chr(ord(x) + 3)
print(ch)
SyntaxError: multiple statements found while compiling a single statement


x = input("Enter a character: ")
Enter a character: A
ch = chr(ord(x) + 3)
print(ch)
D


ord('Z') - ord('A')
25

title = "Chapter " + 1
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    title = "Chapter " + 1
TypeError: can only concatenate str (not "int") to str


title = "Chapter " + "1"
title
'Chapter 1'


No = 1

title = "Chapter " + No
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    title = "Chapter " + No
TypeError: can only concatenate str (not "int") to str

title = "Chapter " + str(No)
title
'Chapter 1'
No
1
type(No)
<class 'int'>

No = str(No)

No
'1'
type(No)
<class 'str'>


s = '2 ' + '3'
s
'2 3'


s = '2' + ' ' + '3'
s
'2 3'

============ RESTART: D:/199/7_3/22.11.14/Compute change.py ============
Enter an amount, for example, 11.56: 11.56
Your amount 11.56 consists of
 	 
 	 
 	 
 	 
 	 
 	 
 	 


============ RESTART: D:/199/7_3/22.11.14/Compute change.py ============
Enter an amount, for example, 11.56: 11.56
Your amount 11.56 consists of
 	 11 laris
 	 50 tetris
 	 20 tetris
 	 10 tetris
 	 5 tetris
 	 2 tetris
 	 tetris


============ RESTART: D:/199/7_3/22.11.14/Compute change.py ============
Enter an amount, for example, 11.56: 11.56
Your amount 11.56 consists of
 	 11 laris
 	 50 tetris
 	 20 tetris
 	 10 tetris
 	 5 tetris
 	 2 tetris
 	 tetris


============ RESTART: D:/199/7_3/22.11.14/Compute change.py ============
Enter an amount, for example, 11.56: 11.56
Your amount 11.56 consists of
 	 11 laris
 	 1 50 tetris
 	 20 tetris
 	 10 tetris
 	 5 tetris
 	 2 tetris
 	 tetris


============ RESTART: D:/199/7_3/22.11.14/Compute change.py ============
Enter an amount, for example, 11.56: 11.56
Your amount 11.56 consists of
 	 11 laris
 	 1 50 tetris
 	 0 20 tetris
 	 10 tetris
 	 5 tetris
 	 2 tetris
 	 tetris


============ RESTART: D:/199/7_3/22.11.14/Compute change.py ============
Enter an amount, for example, 11.56: 11.56
Your amount 11.56 consists of
 	 11 laris
 	 1 50 tetris
 	 0 20 tetris
 	 0 10 tetris
 	 1 5 tetris
 	 0 2 tetris
 	 1 tetris

>>> 
============ RESTART: D:/199/7_3/22.11.14/Compute change.py ============
Enter an amount, for example, 11.56: 1589.93
Your amount 1589.93 consists of
 	 1589 laris
 	 1 50 tetris
 	 2 20 tetris
 	 0 10 tetris
 	 0 5 tetris
 	 1 2 tetris
 	 1 tetris

>>> 
============ RESTART: D:/199/7_3/22.11.14/Compute change.py ============
Enter an amount, for example, 11.56: 1.88
Your amount 1.88 consists of
 	 1 laris
 	 1 50 tetris
 	 1 20 tetris
 	 1 10 tetris
 	 1 5 tetris
 	 1 2 tetris
 	 1 tetris

