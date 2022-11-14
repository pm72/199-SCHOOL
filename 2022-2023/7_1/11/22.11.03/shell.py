Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4
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
>>> abs(-25)
25
>>> abs(125)
125
>>> +3
3
>>> -6
-6
>>> 
>>> 
>>> max(15, 23, 21, 10, 26, 6)
26
>>> min(15, 23, 21, 10, 26, 6)
6
