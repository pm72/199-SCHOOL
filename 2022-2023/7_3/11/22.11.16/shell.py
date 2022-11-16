Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 3
id(x)
2972974514480
id(3)
2972974514480
type(x)
<class 'int'>

f = 3.0
id(f)
2973014042768
type(f)
<class 'float'>

s = 'welcome'

type(s)
<class 'str'>
id(s)
2973015678384


s = "welcome"
s.upper()
'WELCOME'
s
'welcome'


s.lower()
'welcome'

s.title()
'Welcome'
s
'welcome'

s = "welocome to python"
s.title()
'Welocome To Python'

s.capitalize()
'Welocome to python'



s = "   welcome    "
s
'   welcome    '
s.upper()
'   WELCOME    '

s.strip()
'welcome'
s
'   welcome    '


s = "Welcome to python.\n"
s
'Welcome to python.\n'
s.strip()
'Welcome to python.'
s
'Welcome to python.\n'

s = s.strip()
s
'Welcome to python.'


s = "Welcome to python.\nIt is funny"
s
'Welcome to python.\nIt is funny'
print(s)
Welcome to python.
It is funny

s.strip()
'Welcome to python.\nIt is funny'


s = "***python***"
s.strip()
'***python***'

s.strip('*')
'python'


s = "***python***     "
s.strip('*')
'python***     '

s.strip()
'***python***'
s.strip('*')
'python***     '


s = s.strip()
s
'***python***'
s.strip('*')
'python'


s = '**python****       '
s.strip('\n')
'**python****       '
s.strip('p')
'**python****       '
s.strip('*')
'python****       '


s = s.strip()
s = s.strip('*')
s
'python'
s = s.strip('p')
s
'ython'


s = '**python****       '
s = s.strip('**')
s
'python****       '


s = '**python****       '
s = s.strip()
s
'**python****'
s.strip('**')
'python'
s.strip('*************')
'python'
s
'**python****'



s = "Pyrhon ******"
s.strip(' *')
'Pyrhon'


s = "    Python. "
s.lstrip()
'Python. '
s.rstrip()
'    Python.'


" \tGood\tMorning\n".strip()
'Good\tMorning'


s = 'Good\tMorning'




amount = 12618.98
interestRate = 0.0013
interest = amount * interestRate

print("Interest is", interest)
Interest is 16.404674

print("Interest is", round(interest, 2))
Interest is 16.4


print(f"Interest is {interest}")
Interest is 16.404674
Interest is 16.404674
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    Interest is 16.404674
NameError: name 'Interest' is not defined. Did you mean: 'interest'?
>>> 
>>> 
>>> 
>>> x = 5
>>> y = 8
>>> print(x, "+", y, "=", x + y)
5 + 8 = 13
>>> 
>>> print(f"{x} + {y} = {x + y}")
5 + 8 = 13
>>> 
>>> 
>>> print("Interest is", interest)
Interest is 16.404674
>>> 
>>> print(f"interest is{interest}")
interest is16.404674
>>> print(f"interest is{interest:.2f}")
interest is16.40
>>> 
>>> print(f"interest is{interest:.1f}")
interest is16.4
>>> print(f"interest is{interest:.3f}")
interest is16.405
>>> print(f"interest is{interest:.4f}")
interest is16.4047
