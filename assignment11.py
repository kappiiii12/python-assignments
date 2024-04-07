"""
1. Write a python script to print True if the string 'my' is a member in a string entered by user.

2. Write a python script to input two strings from the user and display whether 
the two variables referred to the same object or not.
Print True or False.

3. What will be the output of the python expression 5>10<5?

4. What will be the output of the python expression “Red” and “White”?

5. What will be the output of the python expression True or False?"""
#solution 1
s=input()
print('my' in s)
#solution 2
a=5
b=5
print(a is b)
#solution 3--false
print(5>10<5)
#solution 4
print("red"and"white")
#solution 5
print(True or False)
