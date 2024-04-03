"""
1. Write a python script to calculate simple interest.

2. Write a python script to calculate area of a rectangle.

3. Write a python script to calculate average of three numbers entered by user.

4. Write a python script to calculate volume of a cuboid.

5. Write a python script to take two numbers from user (say x and y), 
now calculate xy and display the result."""
 #solution 1
p=int(input("enter principle"))
t=int(input(" enter time"))
r=int(input("enter rate"))
print("simple interesr =",p*t*r/100)
#solution 2
l=int(input("enter lenght"))
w=int(input("enter width"))
print("area of rectangle =",l*w)
#solution 3
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
print("everage = ",(a+b+c)/3)
#solution 4
l=int(input("enter lenght"))
w=int(input("enter width"))
h=int(input("enter height"))
print("volume of cuboid =",l*w*h)
#solution 5
x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
print("xy = ",x*y)

