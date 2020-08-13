Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> int
<class 'int'>
>>> a
10
>>> 10 == int
False
>>> type(a) == int
True
>>> int(0)
0
>>> int(24)
24
>>> int(False)
0
>>> a=10
>>> if type(a) ==int:
	print("labi")
else:
	print("slikti")

	
labi
>>> a="10"
>>> 
>>> if type(a) == int:
	print("labi")
else:
	print("slikti")

	
slikti
>>> a=5.5
>>> type(a)
<class 'float'>
>>> if type(a) == int:
print("labi")
SyntaxError: expected an indented block
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
        print("ari labi")
else:
	print("slikti")

	
ari labi
>>> a=10
>>> f type(a) == int:
	print("labi")
else:
	print("slikti")
	
SyntaxError: invalid syntax
>>> if type(a) == int:
	print("labi")
elif type(a) == float:
        print("ari labi")
else:
	print("slikti")

	
labi
>>> print ("aaa bbb ccc")
aaa bbb ccc
>>> print ("aaa \n bbb \n ccc")
aaa 
 bbb 
 ccc
>>> 
