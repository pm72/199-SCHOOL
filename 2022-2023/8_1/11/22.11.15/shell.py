Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
ord('A')
65
ord('B')
66
ord('a')
97
ord('a') - ord('A')
32
ord('x') - ord('X')
32
ord('s') - ord('C')
48

chr(65)
'A'
chr(0)
'\x00'
chr(10)
'\n'
chr(13)
'\r'
chr(128)
'\x80'


\u10d0
SyntaxError: unexpected character after line continuation character


'\u10d0'
'ა'
'\u10do\u10d1\u10d2...'
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-4: truncated \uXXXX escape

'\u10d0\u10d1\u10d2...'
'აბგ...'


'პაატა'
'პაატა'


print("\u03b1 = 60\u00b0")
α = 60°

print("α = 45°")
α = 45°



"sdsdd sfffssf"
'sdsdd sfffssf'
'sdsd sdfghdrg dfhrhdbh'
'sdsd sdfghdrg dfhrhdbh'

print("He said, "John's program is easy to read"")
      
SyntaxError: unterminated string literal (detected at line 1)


# '\n'  '\t'  '\u'  '\r'  '\"'  '\''  '\\'
      
print("He said, \"John's program is easy to read")
      
He said, "John's program is easy to read

print("He said, \"John's program is easy to read\"")
...       
He said, "John's program is easy to read"
>>> 
>>> print('He said, "John\'s program is easy to read"')
...       
He said, "John's program is easy to read"
>>> 
>>> print("He said, 'John\'s program is easy to read'")
...       
He said, 'John's program is easy to read'
>>> 
>>> 
>>> print("d:\nile\my_programs\1.py")
...       
d:
ile\my_programs.py
>>> 
>>> print("d:\\nile\\my_programs\\1.py")
...       
d:\nile\my_programs\1.py
>>> 
>>> 
>>> print(r"d:\nile\my_programs\1.py")
...       
d:\nile\my_programs\1.py
>>> 
>>> 
>>> 
