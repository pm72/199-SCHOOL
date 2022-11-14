Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math as m
>>> 
>>> m.degrees(1.289)
73.85425979236311
>>> 73.85425979236311
73.85425979236311
>>> 
>>> 
>>> m.ceil(-2.5)
-2
>>> 
>>> m.floor(-2.5)
-3
>>> 
>>> round(3.5)
4
>>> 
>>> round(4.5)
4
>>> 
>>> m.fabs(2.5)
2.5
>>> m.fabs(2)
2.0
>>> m.fabs(-2)
2.0

m.ceil(2.5)
3
m.floor(2.5)
2


round(m.fabs(-2.5))
2

round(2.5)
2
round(3.5)
4
round(4.5)
4

m = m.radians(47)
m
0.8203047484373349

import math as mt
mt.degrees(m)
47.0


angle = mt.degrees(mt.pi / 7)
angle
25.714285714285715


ch = 'c'
type(ch)
<class 'str'>
text = "Welcome"
type(text)
<class 'str'>

text = 'Welcome there!'
type(text)
<class 'str'>
text = ''
text
''
type(text)
<class 'str'>


2**32
4294967296
2**16
65536


\u10d0
SyntaxError: unexpected character after line continuation character


\u10D0
SyntaxError: unexpected character after line continuation character

'\u10d0'
'ა'
'\u10d1'
'ბ'
print("\u10d0\u10d1")
აბ
print("\u00a7\u10d0\u10d1")
§აბ
print("\u03b1\u03b2")
αβ


print("Display greek symbol alpha: \u03ba")
Display greek symbol alpha: κ
print("Display greek symbol alpha: \u03b0")
Display greek symbol alpha: ΰ
print("Display greek symbol alpha: \u03b2")
Display greek symbol alpha: β
print("Display greek symbol alpha: \u03b1")
Display greek symbol alpha: α


print('💙')
💙
print('\u2665')
♥

'🥰'
'🥰'
print('🥰')
🥰


ord(97)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    ord(97)
TypeError: ord() expected string of length 1, but int found
ord('a')
97
ord('A')
65

chr(65)
'A'
chr(65 + 32)
'a'
chr(65+25)
'Z'
chr(65+25+32)
'z'
'z'
'z'
chr(64 + 26)
'Z'
chr(90)
'Z'


ord('a') - ord('A')
32


chr(128)
'\x80'
ord(chr(128))
128
128
128


for i in range(128):
    print(f"{i}  ==>  {chr(i)}")

    
0  ==>  
1  ==>  
2  ==>  
3  ==>  
4  ==>  
5  ==>  
6  ==>  
7  ==>  
8  ==>  
9  ==>  	
10  ==>  

11  ==>  

12  ==>  

13  ==>  
14  ==>  
15  ==>  
16  ==>  
17  ==>  
18  ==>  
19  ==>  
20  ==>  
21  ==>  
22  ==>  
23  ==>  
24  ==>  
25  ==>  
26  ==>  
27  ==>  
28  ==>  

29  ==>  

30  ==>  

31  ==>  
32  ==>   
33  ==>  !
34  ==>  "
35  ==>  #
36  ==>  $
37  ==>  %
38  ==>  &
39  ==>  '
40  ==>  (
41  ==>  )
42  ==>  *
43  ==>  +
44  ==>  ,
45  ==>  -
46  ==>  .
47  ==>  /
48  ==>  0
49  ==>  1
50  ==>  2
51  ==>  3
52  ==>  4
53  ==>  5
54  ==>  6
55  ==>  7
56  ==>  8
57  ==>  9
58  ==>  :
59  ==>  ;
60  ==>  <
61  ==>  =
62  ==>  >
63  ==>  ?
64  ==>  @
65  ==>  A
66  ==>  B
67  ==>  C
68  ==>  D
69  ==>  E
70  ==>  F
71  ==>  G
72  ==>  H
73  ==>  I
74  ==>  J
75  ==>  K
76  ==>  L
77  ==>  M
78  ==>  N
79  ==>  O
80  ==>  P
81  ==>  Q
82  ==>  R
83  ==>  S
84  ==>  T
85  ==>  U
86  ==>  V
87  ==>  W
88  ==>  X
89  ==>  Y
90  ==>  Z
91  ==>  [
92  ==>  \
93  ==>  ]
94  ==>  ^
95  ==>  _
96  ==>  `
97  ==>  a
98  ==>  b
99  ==>  c
100  ==>  d
101  ==>  e
102  ==>  f
103  ==>  g
104  ==>  h
105  ==>  i
106  ==>  j
107  ==>  k
108  ==>  l
109  ==>  m
110  ==>  n
111  ==>  o
112  ==>  p
113  ==>  q
114  ==>  r
115  ==>  s
116  ==>  t
117  ==>  u
118  ==>  v
119  ==>  w
120  ==>  x
121  ==>  y
122  ==>  z
