Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
NOT

not True = False
not False = True

not 5 = False
not 0 = True

'''
'\nNOT\n\nnot True = False\nnot False = True\n\nnot 5 = False\nnot 0 = True\n\n'

not 0
True

not 8
False

not -1
False


not (5 > 3)
False

not 5 > 3
False

not 5 < 3
True


not 5 < not 3
SyntaxError: invalid syntax

not 5 < (not 3)
True

(not 5) < (not 3)
False

(not 5) == (not 3)
True


'''
AND

False and False = False     0 * 0 = 0
False and True = False      0 * 1 = 0
True and False = False      1 * 0 = 0
True and True = True        1 * 1 = 1
'''
'\nAND\n\nFalse and False = False     0 * 0 = 0\nFalse and True = False      0 * 1 = 0\nTrue and False = False      1 * 0 = 0\nTrue and True = True        1 * 1 = 1\n'


'''
... OR
... 
... False or False = False     0 + 0 = 0
... False or True = True       0 + 1 = 0
... True or False = True       1 + 0 = 0
... True or True = True        1 + 1 = 1
... 
... '''
'\nOR\n\nFalse or False = False     0 + 0 = 0\nFalse or True = True       0 + 1 = 0\nTrue or False = True       1 + 0 = 0\nTrue or True = True        1 + 1 = 1\n\n'

>>> 
>>> a = 5
>>> b = 2
>>> 
>>> a > b and b != 2 * a
True
>>> 
>>> a > b and b == 2 * a
False
>>> 
>>> 
>>> a > b or b == 2 * a
True
>>> 
>>> 
