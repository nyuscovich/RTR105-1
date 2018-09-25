Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
10
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 10
>>> vars()
{'mans_mainiigais': 10, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainiigais
10
>>> mans_mainiigais = input("Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: ")
Cienījamais lietotāj, lūdzu, ievadi vienu skaitli: 20
>>> vars()
{'mans_mainiigais': 20, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> type(mans_mainiigais)
<type 'int'>
>>> 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi skaitli: 5
>>> vars()
{'mans_mainiigais': 5, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi skaitli: 8
>>> vars()
{'mans_mainiigais': 8, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> vars()
{'mans_mainiigais': 8, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180925.py', '__package__': None, 'x': 64, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi skaitli: 89
mans_mainiigais = 
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi skaitli: 156
mans_mainiigais = 156
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi skaitli: 12
mans_mainiigais = 12
vai Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi skaitli: 12
mans_mainiigais = 12
respektīvi, Tu esi ievadījis skaitli: 12
vēl atmiņā tagad ir arī mainīgais x = 144
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 8.6549
mans_mainiigais =      8.655
respektīvi, Tu esi ievadījis skaitli:     8.6549
vēl atmiņā tagad ir arī mainīgais x =      74.9072940
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 7.8
mans_mainiigais =      7.800
respektīvi, Tu esi ievadījis skaitli:     7.8000
vēl atmiņā tagad ir arī mainīgais x =      60.8400000
>>> type(mans_mainiigais)
<type 'float'>
>>> type(x)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 8
mans_mainiigais =      8.000
respektīvi, Tu esi ievadījis skaitli:     8.0000
vēl atmiņā tagad ir arī mainīgais x =      64.0000000
>>> type(mans_mainiigais)
<type 'int'>
>>> type(x)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 8.
mans_mainiigais =      8.000
respektīvi, Tu esi ievadījis skaitli:     8.0000
vēl atmiņā tagad ir arī mainīgais x =      64.0000000
>>> type(mans_mainiigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi daļskaitli: 8
mans_mainiigais =      8.000
respektīvi, Tu esi ievadījis skaitli:     8.0000
vēl atmiņā tagad ir arī mainīgais x =      64.0000000
>>> type(mans_mainiigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: aaaaaa

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 2, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: aaaaa
mans_mainiigais = aaaaa
respektīvi, Tu esi ievadījis rindu: aaaaa

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180925.py", line 8, in <module>
    print("vēl atmiņā tagad ir arī mainīgais x = %s"%(x))
NameError: name 'x' is not defined
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180925.py ===============
Cienījamais lietotāj, lūdzu, ievadi simbolu rindu: Aaaaaaa
mans_mainiigais = Aaaaaaa
respektīvi, Tu esi ievadījis rindu: Aaaaaaa
>>> type(mans_mainiigais)
<type 'str'>
>>> 

