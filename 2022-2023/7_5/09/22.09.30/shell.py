Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> '1' + '5'
'15'
>>> 1 + 5
6
>>> 2.3 + 9
11.3
>>> 1.0 + 9
10.0
>>> 
=========== RESTART: D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py ===========
The area of the citcle with radius 20.58 is 1330.5777188759998
The length of the citcle with radius 20.58 is 129.3078444
>>> 
=========== RESTART: D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py ===========
The area of the citcle with radius 20.58 is 1330.58
The length of the citcle with radius 20.58 is 129.31
>>> area
1330.58
>>> 
=========== RESTART: D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py ===========
The area of the citcle with radius 20.58 is 1330.58
The length of the citcle with radius 20.58 is 129.31
>>> area
1330.5777188759998
>>> length
129.3078444
>>> 
=========== RESTART: D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py ===========
The area of the citcle with radius 20 is 1256.64
The length of the citcle with radius 20 is 125.66
>>> 
=========== RESTART: D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py ===========
25
Traceback (most recent call last):
  File "D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py", line 8, in <module>
    area = PI * radius ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 
=========== RESTART: D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py ===========
Enter the radius: 20
Traceback (most recent call last):
  File "D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py", line 8, in <module>
    area = PI * radius ** 2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> radius
'20'
>>> type(radius)
<class 'str'>
>>> 
>>> init('125')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    init('125')
NameError: name 'init' is not defined
>>> int('125')
125
>>> type(int('125'))
<class 'int'>
>>> int('12.5')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    int('12.5')
ValueError: invalid literal for int() with base 10: '12.5'
>>> 
>>> int(2.58)
2
>>> int(2.98)
2
>>> float('1.247')
1.247
>>> type(float('1.247'))
<class 'float'>
>>> float('1')
1.0
>>> 1 == 1.0
True
>>> 1 == '1'
False
>>> eval('45')
45
>>> type(eval('45'))
<class 'int'>
>>> type(eval('4.5'))
<class 'float'>
>>> eval(4.5)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    eval(4.5)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> eval('4.5')
4.5
>>> 
=========== RESTART: D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py ===========
Enter the radius: 25
The area of the citcle with radius 25 is 1963.49
The length of the citcle with radius 25 is 157.08
>>> 
=========== RESTART: D:\199\7_5\22.9.30\წრის ფართობის გამოთვლა.py ===========
Enter the radius: 2.39
The area of the citcle with radius 2.39 is 17.95
The length of the citcle with radius 2.39 is 15.02
>>> 
>>> 
>>> x = int(input("Enter a number: "))
Enter a number: 5
>>> x
5
>>> type(x)
<class 'int'>
>>> 
>>> x = int(input("Enter a number: "))
Enter a number: 2.58
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x = int(input("Enter a number: "))
ValueError: invalid literal for int() with base 10: '2.58'
>>> 
>>> x = float(input("Enter a number: "))
Enter a number: 25
>>> type(x)
<class 'float'>
>>> x
25.0
>>> x = float(input("Enter a number: "))
Enter a number: 2.89
>>> x
2.89
>>> 
>>> 
>>> x = eval(input("Enter a number: "))
Enter a number: 25
>>> x
25
>>> 
>>> x = eval(input("Enter a number: "))
Enter a number: 4.58
>>> x
4.58
>>> x = eval(input("Enter a number: "))
Enter a number: 4.0
>>> x
4.0
>>> type(x)
<class 'float'>
>>> 
>>> 
>>> 6/2
3.0
>>> 6/4
1.5
>>> 9/5
1.8
>>> 6/5
1.2
>>> 2 + 6/5
3.2
>>> 2 + 6/6
3.0
>>> 
============ RESTART: D:/199/7_5/22.9.30/საშუალო არითმეტიკული.py ============
Enter number1: 1
Enter number2: 2
Enter number3: 3
The average of 1 2 3 is 2.0
>>> 
============ RESTART: D:/199/7_5/22.9.30/საშუალო არითმეტიკული.py ============
Enter number1: 1.58
Enter number2: 0.36984
Enter number3: 0.147
The average of 1.58 0.36984 0.147 is 0.6989466666666666
>>> 
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> 
>>> temp = x
>>> x = y
>>> y = temp
>>> 
>>> x, y
(15, 20)
>>> 
>>> 
>>> x = 20
>>> y = 15
>>> 
>>> x, y
(20, 15)
>>> 
>>> x, y = y, x
>>> 
>>> x, y
(15, 20)
>>> 
>>> 
>>> x, y = 2, 9
>>> x, y
(2, 9)
>>> 
