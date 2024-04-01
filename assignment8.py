"""1. Write a python script to take your name as input from the user and then print it.

2. Write a python script to take input two numbers form the user, 
then calculate their sum and display the result.

3. Write a python script which takes the radius from the user and display area of the circle.

4. Write a python script to calculate square of a number. Number is entered by the user.

5. Write a python script which takes a character from the user and display its unicode.
"""
#solution 1
a=input("enter your name")
print(a)
#solution 2
x=int(input("enter first number"))
y=int(input("enter second number"))
print(x+y)
#solution 3
r=int(input("enter radius"))
print(3.14*r*r)
#solution 4
s=int(input("enter any number"))
print("square",s*s,sep='=')
#solution 5
k=input("enter any character")
print(ord(k))
