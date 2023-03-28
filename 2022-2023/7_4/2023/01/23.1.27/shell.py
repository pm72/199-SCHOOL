Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random as r
r.randrange(1, 1)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    r.randrange(1, 1)
  File "C:\Program Files\Python310\lib\random.py", line 353, in randrange
    raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (1, 1, 0)

r.randrange(1, 6)
1
r.randrange(1, 6)
1
r.randrange(1, 6)
4
r.randrange(1, 6)
2

range(1, 8)
range(1, 8)
list(range(1, 8))
[1, 2, 3, 4, 5, 6, 7]


r.random()
0.19565101393574735
r.random()
0.2813108382395725


r.uniform(5, 7)
6.134889041589231
r.uniform(5, 7)
5.024044971189008
r.uniform(5, 7)
6.457490221582086

r.uniform(5.247, 5.3)
5.279422297713534



for i in range(20):
    print(r.uniform(5.1, 5.2))

    
5.1487158070454155
5.1383422355371415
5.115549760848049
5.117584686074469
5.169058864613964
5.165999905386075
5.167882610481434
5.163453151442611
5.128496690885069
5.198393155513395
5.152857335884926
5.158190679844472
5.159916371706083
5.1546974616748855
5.1154604059878785
5.172074447027805
5.1135470613614995
5.127858077927994
5.173413340144982
5.164257782699543


for i in range(20):
    print(r.randint(5, 8))

    
5
5
6
5
5
8
8
5
7
8
5
6
7
6
7
6
7
7
8
7

for i in range(20):
    print(r.randint(5, 100))

    
10
38
50
53
61
56
8
77
51
81
64
79
9
73
43
72
52
63
77
56


for i in range(20):
    print(r.uniform(5, 8))

    
6.12957060402036
5.682906978006425
5.857662379219405
6.591346466287346
7.6471843481544575
6.089844168924181
5.4268776698637655
5.307564174274007
5.163983127149455
5.9584466081583765
5.341753830298217
7.0123144598481435
7.1247820034081375
7.147128049822351
7.056843443320923
7.9539475697522075
7.615334471562491
5.721125430659147
7.303828183654623
5.887060562079746

>>> 
>>> 
>>> 
======= RESTART: D:/199/7_4/2023/01/simple_if_demo.py ======
Enter an integer: 25
Hi five!
>>> 
======= RESTART: D:/199/7_4/2023/01/simple_if_demo.py ======
Enter an integer: 8
Hi even!
>>> 
======= RESTART: D:/199/7_4/2023/01/simple_if_demo.py ======
Enter an integer: 30
Hi five!
Hi even!
>>> 
======= RESTART: D:/199/7_4/2023/01/simple_if_demo.py ======
Enter an integer: 9
>>> 
======= RESTART: D:/199/7_4/2023/01/simple_if_demo.py ======
Enter an integer: 12
Even
>>> 
======= RESTART: D:/199/7_4/2023/01/simple_if_demo.py ======
Enter an integer: 21
Odd
