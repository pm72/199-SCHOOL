Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
3
3
id(3)
2336139903280
2336139903280
2336139903280


x = 3
id(x)
2336139903280
print(x)
3
type(x)
<class 'int'>
type(3)
<class 'int'>


s = "welcome"
s.upper()
'WELCOME'
s
'welcome'

s = s.upper()
s
'WELCOME'

s.lower()
'welcome'
s
'WELCOME'

s.title()
'Welcome'

s = s + " to python".upper()
s
'WELCOME TO PYTHON'
s.title()
'Welcome To Python'

s.capitalize()
'Welcome to python'

s += ". it is funny"
s = s.lower()

s
'welcome to python. it is funny'
s.capitalize()
'Welcome to python. it is funny'



s = "    welcome to python       "
s
'    welcome to python       '

s.strip()
'welcome to python'
s
'    welcome to python       '

s.lstrip()
'welcome to python       '
s.rstrip()
'    welcome to python'

# .strip()    ' ' + '\n'  '\t'

s = "\t\t\twelcome to Python\n\n"
print(s)
			welcome to Python


>>> s.strip()
'welcome to Python'
>>> 
>>> 
>>> s = "****welcome*********"
>>> s.strip()
'****welcome*********'
>>> s.strip('*')
'welcome'
>>> s = "****welcome *********"
>>> s.strip('*')
'welcome '
>>> s.strip(' *')
'welcome'
>>> s.strip('* ')
'welcome'
>>> s.strip('* !')
'welcome'
>>> s
'****welcome *********'
>>> s.strip('* w')
'elcome'
>>> 
>>> 
>>> " \tGood\tMorning\n".strip()  # Good\tMorning
'Good\tMorning'
