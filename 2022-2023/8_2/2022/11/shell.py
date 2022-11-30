Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 25
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 20
Traceback (most recent call last):
  File "D:\199\8_2\22.9.30\წრის ფართობი.py", line 7, in <module>
    area = PI * radius ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> radius
'20'
>>> type(radius)
<class 'str'>
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 20
1256.636
125.6636
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 20.58
1330.5777188759998
129.3078444
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 21.298
The area of the circle of radius 21.298 is 1425.0403161983597
The perimeter of the circle of radius 21.298 is 133.81916764

================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 21.298
The area of the circle of radius 21.298 is 1425.04
The perimeter of the circle of radius 21.298 is 133.82

================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 1.225f
Traceback (most recent call last):
  File "D:\199\8_2\22.9.30\წრის ფართობი.py", line 7, in <module>
    radius = eval(input("Enter the radius: "))
  File "<string>", line 1
    1.225f
         ^
SyntaxError: unexpected EOF while parsing
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 2.569.
Ilegal input
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: w
Traceback (most recent call last):
  File "D:\199\8_2\22.9.30\წრის ფართობი.py", line 8, in <module>
    radius = eval(input("Enter the radius: "))
  File "<string>", line 1, in <module>
NameError: name 'w' is not defined

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\199\8_2\22.9.30\წრის ფართობი.py", line 21, in <module>
    except asSyntaxError as error:
NameError: name 'asSyntaxError' is not defined
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 6.5.5
unexpected EOF while parsing (<string>, line 1)
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 2.5g
Illegeal input.
Please enter the valid number.
>>> 
================ RESTART: D:\199\8_2\22.9.30\წრის ფართობი.py ================
Enter the radius: 25v
Illegeal input.
Please enter the valid number.

>>> 
