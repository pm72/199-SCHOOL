Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================== RESTART: D:\199\7_7\22.11.03\2_18.py =================
Current time is 8:32:29 GMT

================= RESTART: D:\199\7_7\22.11.03\2_18.py =================
Enter your time zone: 4
Current time is 12:34:19 GMT4

================= RESTART: D:\199\7_7\22.11.03\2_18.py =================
Enter your time zone: 0
Current time is 8:34:33 GMT0

================= RESTART: D:\199\7_7\22.11.03\2_18.py =================
Enter your time zone: -7
Current time is 1:34:50 GMT-7

================= RESTART: D:\199\7_7\22.11.03\2_18.py =================
Enter your time zone: 
0
Current time is 8:35:7 GMT0

================= RESTART: D:\199\7_7\22.11.03\2_18.py =================
Enter your time zone: 4
Current time is 12:36:3 GMT4



x1, y1, x2, y2, x3, y3 = eval(input("Enter three points for a triangle: "))
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4

a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

p = (a + b + c) / 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print("The area of the triangle is", round(s, 2))
The area of the triangle is 33.6
>>> 
>>> 
>>> 
>>> a = eval(input("Enter the side: "))
Enter the side: 5.5
>>> 
>>> area = ((3 * (3 ** 0.5)) / (2)) * a ** 2
>>> 
>>> print("The area of the hexagon is", round(area, 2))
The area of the hexagon is 78.59
>>> 
>>> 
>>> pounds = eval(input("Enter weight in pounds: "))
Enter weight in pounds: 95.5
>>> 
>>> inches = eval(input("Enter height in inches: "))
Enter height in inches: 50
>>> 
>>> kg = pounds * 0.45359237
>>> m = inches * 0.0254
>>> 
>>> bmi = kg / m ** 2
>>> 
>>> print("BMI is", round(bmi))
BMI is 27
>>> 
>>> 
