Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'a'
'a'
"a"
'a'

'Paata'
'Paata'
"PAATA"
'PAATA'


ord('A')
65
ord('a')
97
ord('b')
98
ord('0')
48

ord('a') - ord('A')
32
ord('b') - ord('B')
32
ord('b') - ord('S')
15


chr(65)
'A'
chr(97)
'a'
chr(13)
'\r'
chr(10)
'\n'
2**16
65536

chr(0)
'\x00'



'\u0065'
'e'


'\u10d0'
'ა'
'\u10d1'
'ბ'
print("\u10d0\u10d1\u10d2...")
აბგ...


'\u03b1'
'α'


import math aS m
SyntaxError: invalid syntax

import math as m
print("\u03co =", m.pi)
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-4: truncated \uXXXX escape
print("\u03c0 =", m.pi)
π = 3.141592653589793

print("\u03b1 =", 60, "\u00b0")
α = 60 °

print("\u03b1 =", str(60) + "\u00b0")
α = 60°

print("α =", str(60) + '°')
α = 60°

print("β =", str(90) + '°')
β = 90°
print("δ =", str(30) + '°')
δ = 30°


print("\u6B22\u8FCE \u03b1 \u03b2 \u03b3")
欢迎 α β γ


print("He said, "John's program is easy to read"")
      
SyntaxError: unterminated string literal (detected at line 1)

'\t'
      
'\t'
print('\t')
      
	
print('a\tb\t')
      
a	b	
print('a\tb\tc')
      
a	b	c
print('a    b    c')
      
a    b    c


print('\"')
      
"
print('\')
      
SyntaxError: unterminated string literal (detected at line 1)
print('\'')
      
'

print("He said, \"John's program is easy to read\"")
      
He said, "John's program is easy to read"

>>> print('He said, "John\'s program is easy to read"')
...       
He said, "John's program is easy to read"
>>> 
>>> print("He said, 'John\'s program is easy to read'")
...       
He said, 'John's program is easy to read'
>>> He said, 'John's program is easy to read'
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> 
>>> 
>>> print("c:\nile\my_files\1.py")
...       
c:
ile\my_files.py
>>> print("c:\\nile\\my_files\\1.py")
...       
c:\nile\my_files\1.py
>>> 
>>> 
>>> print("c:\\nile\my_files\1.py")
...       
c:\nile\my_files.py
>>> 
>>> 
>>> 
