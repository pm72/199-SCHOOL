Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ==============
Enter a radius: -5
Wrong input. Enter a positive.

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 2.56

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 2.57
The area is 20.74990531769522

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: -5
Wrong input. Enter a positive.

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 2.57
The area is 20.75



# <, <=, >, >=, ==, !=

a = 5
a
5

a == 5
True
a != 5
False

a < 5
False
a <= 5
True

a > 5
False
 a >= 5
 
SyntaxError: unexpected indent
a >= 5
True


# int, float, str
# bool  => True, False

a = 5
b = 3

a + b != a * b
True

a + (b != a) * b
8


int(2.69)
2

int(True)
1
int(False)
0
int(False)
0

bool(1)
True
bool(12)
True
bool(-1.2)
True
bool(0)
False

bool(0.0)
False

bool("")
False


=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 2.15
The area is 14.52

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 1.89
The area is 11.22

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: -6
Wrong input. Enter a positive.
Traceback (most recent call last):
  File "D:/199/7_6/2023/01/23.1.20/circle_area.py", line 10, in <module>
    print(f"The area is {area:.2f}")
NameError: name 'area' is not defined

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 25
The area is 1963.50

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 0

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 0
The area is 0.00

=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 0
The area is 0.00
>>> 
=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: -6
The area is 0.00
>>> 
=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 5.47
The area is 94.00
>>> 
=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: 2.56
The area is 20.59
0.152587890625
>>> 
=== RESTART: D:/199/7_6/2023/01/23.1.20/circle_area.py ===
Enter a radius: -5
The area is 0.00
Traceback (most recent call last):
  File "D:/199/7_6/2023/01/23.1.20/circle_area.py", line 20, in <module>
    print(m.pi / area)
ZeroDivisionError: float division by zero
