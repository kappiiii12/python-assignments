"""
1. Write a python script to convert a number into str type.

2. Write a python script to print Unicode of the character 'm'

3. Write a python script to print character representation of a given unicode 100.

4. Write a python script to convert a str type data into an int type.
 Also describe when a str type value is not possible to convert into an int type.

5. How to convert an integer value into a bool value?"""
#solution 1
a=10
a=str(a)
print(type(a))
#solution 2
a='A'
print(ord(a))
#solution 3
print(chr(100))
#solution 4
a='10'
print(type(int(a)))
#solution 4
a=10
print(bool(a))