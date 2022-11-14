Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: D:/შემაჯამებელი 1/2_01.py =====================
Enter a degree in Celsius: 43
43 Celsius is 109.4 Fahrenheit
>>> 
===================== RESTART: D:/შემაჯამებელი 1/2_01.py =====================
Enter a degree in Celsius: 43
43Celsius is109.4Fahrenheit
>>> 
===================== RESTART: D:/შემაჯამებელი 1/2_01.py =====================
Enter a degree in Celsius: 43
43***Celsius is***109.4***Fahrenheit
>>> 
===================== RESTART: D:/შემაჯამებელი 1/2_01.py =====================
12
>>> 
===================== RESTART: D:/შემაჯამებელი 1/2_01.py =====================
1 2
>>> 
===================== RESTART: D:/შემაჯამებელი 1/2_01.py =====================
1 2
>>> 
===================== RESTART: D:/შემაჯამებელი 1/2_01.py =====================
>>> 
>>> 
>>> a = input("Enter an integer: ")
Enter an integer: 45
>>> print(a + 15)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(a + 15)
TypeError: must be str, not int
>>> a
'45'
>>> type(a)
<class 'str'>
>>> int(a)
45
>>> eval(a)
45
>>> a = eval(input("Enter an integer: "))
Enter an integer: 45
>>> print(a + 15)
60
>>> a = eval(input("Enter an integer: "))
Enter an integer: 4.5
>>> print(a + 15)
19.5
>>> 
>>> 
>>> 
>>> eval('15')
15
>>> eval('15.25')
15.25
>>> eval(15.25)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    eval(15.25)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> eval('.15')
0.15
>>> eval('15.')
15.0
>>> eval('1.5')
1.5
>>> eval('1.5.')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    eval('1.5.')
  File "<string>", line 1
    1.5.
       ^
SyntaxError: unexpected EOF while parsing
>>> 
>>> 
>>> 
>>> a, b = eval(input("Enter two numbers: "))
Enter two numbers: 15, 25.6
>>> a, b = 15, 25.6
>>> 
>>> radius, length = eval(input("Enter the radius and length of a cylinder: "))
Enter the radius and length of a cylinder: 5.5, 12
>>> radius, length
(5.5, 12)
>>> radius
5.5
>>> length
12
>>> area = 3.14189 * radius ** 2
>>> volume = area * length
>>> volume
1140.5060700000001
>>> round(volume, 2)
1140.51
>>> round(volume, 1)
1140.5
>>> round(volume)
1141
>>> 
