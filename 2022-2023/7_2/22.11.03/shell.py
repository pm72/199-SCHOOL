Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4

a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

p = (a + b + c) / 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("The area of the triangle is", round(s, 2))
The area of the triangle is 33.6


# 2.17 BMI
pounds = eval(input("Enter weight in pounds: "))
Enter weight in pounds: 95.5

inches = eval(input("Enter height in inches: "))
Enter height in inches: 50

kg = pounds * 0.45359237
m = inches * 0.0254

bmi = kg / m ** 2

print("BMI is", round(bmi))
BMI is 27




# მათემატიკური ფუნქციები math
help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.



import math
help(math.fabs)
Help on built-in function fabs in module math:

fabs(x, /)
    Return the absolute value of the float x.



abs(-25)
25
>>> abs(11)
11
>>> 
>>> pow(2, 3)
8
>>> 2 ** 3
8
>>> pow(2, 3, 2)
0
>>> 
>>> help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> pow(2, 3, 3)
2
>>> 
>>> max(15, 25, 3, 18, 21, 8)
25
>>> min(15, 25, 3, 18, 21, 8)
3
