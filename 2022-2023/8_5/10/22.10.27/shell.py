Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x1, y1, x2, y2, x3, y3 = 1.5, -3.4, 4.6, 5, 9.5, -3.4
>>> 
>>> a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
>>> b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
>>> c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
>>> 
>>> p = (a + b + c) / 2
>>> 
>>> s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
>>> 
>>> print("The area of the triangle is", round(s, 2))
The area of the triangle is 33.6
>>> 
>>> 
>>> 
>>> a = eval(input("Enter the side: "))
Enter the side: 5.5
>>> 
>>> area = ((3 * 3 ** 0.5) / 2) * a ** 2
>>> 
>>> print("The area of the hexagon is", round(area, 4))
The area of the hexagon is 78.5918
>>> print("The area of the hexagon is", round(area, 2))
The area of the hexagon is 78.59
>>> 
>>> 
>>> v0, v1, t = 5.5, 50.9, 4.5
>>> 
>>> a = (v1 - v0) / t
>>> 
>>> print("The average acceleration is", round(a, 2))
The average acceleration is 10.09
>>> 
>>> 
>>> a = eval(input("Enter v0, v1, and t: "))
Enter v0, v1, and t: 5.5, 50.9, 4.5
>>> 
>>>  a = (v1 - v0) / t
 
SyntaxError: unexpected indent
>>> a = (v1 - v0) / t
>>> 
>>> print("The average acceleration is", round(a, 2))
The average acceleration is 10.09
>>> 
>>> 
>>> 
>>> 
>>> pounds, inches = 95.5, 50
>>>  kg = pounds * 0,45359237
 
SyntaxError: unexpected indent
>>> kg = pounds * 0,45359237
>>> m = inches * 0.0254
>>> bmi = kg / m ** 2
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    bmi = kg / m ** 2
TypeError: unsupported operand type(s) for /: 'tuple' and 'float'
>>> bmi = kg / m ** 2
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    bmi = kg / m ** 2
TypeError: unsupported operand type(s) for /: 'tuple' and 'float'
>>> kg = pounds * 0.45359237
>>> m = inches * 0.0254
>>> bmi = kg / m ** 2
>>> 
>>> print("BMI is", round(bmi))
BMI is 27
>>> 
>>> 
>>> 
>>> 
