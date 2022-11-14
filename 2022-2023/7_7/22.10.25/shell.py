Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x1, y1 = 2.51, 1.09
>>> x1, y1
(2.51, 1.09)
>>> 
>>> x1, y1 = eval(input("Enter first point's 2D koordinates: "))
Enter first point's 2D koordinates: 25.89, -96.32
>>> x2, y2 = eval(input("Enter second point's 2D koordinates: "))
Enter second point's 2D koordinates: 11.54, -32.89
>>> x3, y3 = eval(input("Enter third point's 2D koordinates: "))
Enter third point's 2D koordinates: 114.72, 35, 28
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x3, y3 = eval(input("Enter third point's 2D koordinates: "))
ValueError: too many values to unpack (expected 2)
>>> x3, y3 = eval(input("Enter third point's 2D koordinates: "))
Enter third point's 2D koordinates: 114.75, 35.28
>>> 
>>> a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
>>> b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
>>> c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
>>> 
>>> p = (a + b + c) / 2
>>> 
>>> s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
>>> 
>>> print("The area of the triangle is", s)
The area of the triangle is 3762.424900000001
>>> print("The area of the triangle is", round(s, 2))
The area of the triangle is 3762.42
>>> 
>>> 
>>> 
>>> "area of Hexagon"
'area of Hexagon'
>>> 
>>> # area of Hexagon
>>> side = eval(input("Enter the side for hexagon: "))
Enter the side for hexagon: 5.5
>>> 
>>> area = (3 * 3**0.5) / 2 * (side) ** 2
>>> 
>>> print("The area of the hexagon is", area)
The area of the hexagon is 78.59180539343781
>>> 
>>> print("The area of the hexagon is", round(area, 2))
The area of the hexagon is 78.59
>>> print("The area of the hexagon is", round(area, 4))
The area of the hexagon is 78.5918
>>> 
