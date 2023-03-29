Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

====================== RESTART: D:/199/7_3/2023/lottery.py =====================
Enter your lottery pick (two digits): 39
Sorry, no match
lottery: 48


====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 47
Sorry, no match
lottery: 16

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 12
Sorry, no match
lottery: 45

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 69
Match one digit: you win $1,000
lottery: 36

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 59
Sorry, no match
lottery: 27

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 14
Sorry, no match
lottery: 86

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 71
Sorry, no match
lottery: 44

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 57
Sorry, no match
lottery: 29

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 26
Match one digit: you win $1,000
lottery: 69

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 38
Sorry, no match
lottery: 22

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 42
Sorry, no match
lottery: 30

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 96
Sorry, no match
lottery: 20

====== RESTART: D:/199/7_3/2023/lottery.py ======
Enter your lottery pick (two digits): 83
Sorry, no match
lottery: 47








x, y = 45, 21
if x > y: print(x)
else: print(y)

45
>>> 
>>> print(f"{x} > {y}" if x > y else f"{x} < {y}")
45 > 21
>>> 
>>> 
>>> x, y = 15, 21
>>> print(f"{x} > {y}" if x > y else f"{x} < {y}")
15 < 21
>>> 

>>> age = 25
>>> ticketPrice = 20 if age >= 16 else 10
>>> ticketPrice
20
>>> 
>>> 
>>> count = 156
>>> print(count if count % 10 == 0 else count, end=' ')
156 
>>> 
>>> count = 100
>>> print(count if count % 10 == 0 else count, end=' ')
100 
>>> 
>>> print(count) if count % 10 == 0 else print(count, end=' ')
100
