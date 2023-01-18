Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py =============
Enter a radius: -9
Wrong input. Enter a positive number!..

= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Enter a radius: 5.69

= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Enter a radius: 5.69
The area is 101.71

= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Enter a radius: -9
Wrong input. Enter a positive number!..


  a = 9
  
SyntaxError: unexpected indent

= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Enter a radius: 2.36
The area is 17.50

Done!

= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Enter a radius: -5
Wrong input. Enter a positive number!..

Done!

= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Enter a radius: 2.03
The area is 12.95

Done!

= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Enter a radius: -9= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Traceback (most recent call last):
  File "D:/199/7_3/2023/01/23.1.18/circle_radius.py", line 3, in <module>
    radius = eval(input("Enter a radius: "))
  File "<string>", line 1
    -9= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
                                 ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers



= RESTART: D:/199/7_3/2023/01/23.1.18/circle_radius.py
Enter a radius: -9
Wrong input. Enter a positive number!..
Traceback (most recent call last):
  File "D:/199/7_3/2023/01/23.1.18/circle_radius.py", line 10, in <module>
    print(f"The area is {area:.2f}")
NameError: name 'area' is not defined

= RESTART: D:\199\7_3\2023\01\23.1.18\circle_radius.py
Enter a radius: -9

= RESTART: D:\199\7_3\2023\01\23.1.18\circle_radius.py
Enter a radius: 0

Done!



= RESTART: D:\199\7_3\2023\01\23.1.18\circle_radius.py
Enter a radius: 0
Traceback (most recent call last):
  File "D:\199\7_3\2023\01\23.1.18\circle_radius.py", line 39, in <module>
    print(area)
NameError: name 'area' is not defined

= RESTART: D:\199\7_3\2023\01\23.1.18\circle_radius.py
Enter a radius: 0
0

Done!



= RESTART: D:\199\7_3\2023\01\23.1.18\circle_radius.py
Enter a radius: -5
0

Done!



= RESTART: D:\199\7_3\2023\01\23.1.18\circle_radius.py
Enter a radius: 4.57
The area is 65.61
65.61184841095748

Done!




# <, <=, >, >=. ==, !=

a = 5
a
5

a == 5
True
a != 5
False

# int, float, str
# bool  => True, False

a < 5
False
 a <= 5
 
SyntaxError: unexpected indent
a <= 5
True

a > 5
False

a >= 5
True

a != 5
False

a == 5
True

True + 5
6
False + 5
5

2.5 + 3
5.5

>>> 
>>> int(True)
1
>>> 
>>> int(False)
0
>>> 

>>> bool(0)
False
>>> 
>>> bool(1)
True
>>> 
>>> bool(24)
True
>>> 
>>> bool(2.34)
True
>>> 
>>> bool(-2.34)
True
>>> 
>>> bool("")
False
