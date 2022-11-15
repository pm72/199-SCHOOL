Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math as m
m.pi
3.141592653589793



help(m.acos)
Help on built-in function acos in module math:

acos(x, /)
    Return the arc cosine (measured in radians) of x.
    
    The result is between 0 and pi.



m.pi
3.141592653589793


m.degrees(m.pi)
180.0

============= RESTART: D:/199/7_2/22.11.15/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The three angles are 0.27 1.57 1.3

0.27+1.57+1.3
3.14
0.27+1.3
1.57

============ RESTART: D:/199/7_2/22.11.15/Compute angles.py ============
Enter three points: 1, 1, 6.5, 1, 6.5, 2.5
The three angles are 15.26 90.0 74.74



round(math.fabs(-2.5))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    round(math.fabs(-2.5))
NameError: name 'math' is not defined


round(m.fabs(-2.5))
2


round(2.5)
2
round(3.5)
4
round(4.5)
4


print("My name is Paata")
My name is Paata
print('My name is Paata')
My name is Paata

print('')



print('My name is "Paata"')
My name is "Paata"
print("My name is 'Paata'")
My name is 'Paata'
print('My name is \'Paata\'')
My name is 'Paata'
print("My name is 'Paata'")
My name is 'Paata'
print("My name is "Paata"")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("My name is ", Paata"")
SyntaxError: invalid syntax
>>> print("My name is ", Paata,"")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    print("My name is ", Paata,"")
NameError: name 'Paata' is not defined
>>> 
>>> 
>>> print("My name is \"Paata\"")
My name is "Paata"
>>> 
>>> 
>>> #  '\n'  '\r'  '\t'  '\"'  '\''
>>> 
>>> 
>>> print("A\tB\tC")
A	B	C
>>> 
>>> print("A\tB\tC\n11\t58\t2.589")
A	B	C
11	58	2.589
>>> 
>>> 
>>> print("A\tB\tC\n1.01\t5.898\t2.589")
A	B	C
1.01	5.898	2.589
>>> 
>>> 
>>> 
