Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("He said: "John's programm is funny..."")
      
SyntaxError: unterminated string literal (detected at line 1)

'\n' '\t' '\r' '\"'  '\'' '\\'
      
'\n\t\r"\'\\'
#  '"dffdf dgdgdg"'   "'dffdf' d ddf"  "dfdff \"dfdfd\" ddvg"
      

print("He said: \"John's programm is funny...\"")
      
He said: "John's programm is funny..."

print('He said: "John\'s programm is funny..."')
      
He said: "John's programm is funny..."

print("He said: 'John\'s programm is funny...'")
      
He said: 'John's programm is funny...'


print("d:\nile\my_programs\1.py")
      
d:
ile\my_programs.py

print("d:\\nile\\my_programs\\1.py")
      
d:\nile\my_programs\1.py


int(3.56)
      
3
int('3')
      
3
float(25)
      
25.0
float('25')
      
25.0
float('25.25')
      
25.25
eval('12.56')
      
12.56


str(12.5666)
      
'12.5666'

'12' + '12'
      
'1212'
12 + 12
      
24

'12' + 12
      
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    '12' + 12
TypeError: can only concatenate str (not "int") to str

name = "Paata"
      
age = 50
      

text = "my name is " + name + " and I am " + age + " years..."
      
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    text = "my name is " + name + " and I am " + age + " years..."
TypeError: can only concatenate str (not "int") to str
type(name)
      
<class 'str'>
type(age)
      
<class 'int'>


text = "my name is " + name + " and I am " + 'age' + " years..."
      
text
      
'my name is Paata and I am age years...'

text = "my name is " + name + " and I am " + str(age) + " years..."
      
text
      
'my name is Paata and I am 50 years...'

age
      
50


welcome = "Welcome to python"
      
welcome = welcome + " and it is funny..."
      
welcome
      
'Welcome to python and it is funny...'
>>> 
>>> welcome += " !!!"
...       
>>> welcome
...       
'Welcome to python and it is funny... !!!'
>>> 
>>> 
>>> 
>>> ch = "Chapter"
...       
>>> No = 2
...       
>>> ch + ' ' + str(No)
...       
'Chapter 2'
>>> 
>>> 
>>> 
>>> 11.56 * 100
...       
1156.0
>>> 1156 // 100
...       
11
>>> 1156 % 100
...       
56
