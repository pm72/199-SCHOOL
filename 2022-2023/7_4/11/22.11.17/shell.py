Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = 3
id(n)
2704744382768
id(3)
2704744382768
type(n)
<class 'int'>
n
3
3
3

>>> 
>>> n = 5.9
>>> id(n)
2704779976944
>>> 
>>> n = 3
>>> id(n)
2704744382768
>>> 
>>> 
>>> n = 'PAATA'
>>> id(n)
2704749962288
>>> id('paata')
2704781354416
>>> 
>>> id('PAATA')
2704749962288
>>> 
>>> 
>>> 
>>> s = 'welcome'
>>> 
>>> s.upper()
'WELCOME'
>>> 
>>> s.lower()
'welcome'
