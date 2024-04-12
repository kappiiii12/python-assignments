"""
1. Write a python script to check whether a given number is a three digit number or not.

2. Write a python script to check whether a given number is positive, negative or zero.

3. Write a python script to make a menu driven program in which 
user has to choose one of the option from four given options -
 1) Odd-Even, 2) positive - Non Positive, 3) Simple Interest and
 4) find roots of quadratic equation. Match and execute appropriate code on user selection.

4. Write a python script to take one data from user and evaluate the type of data. 
If the data is of int type then print Monday,
if the data is of float type then print Tuesday,
if the data is of complex type then print Wednesday,
if the data is of type bool then print Thursday.

5. Write a python script to take a string from the user.
If the string is a part of "mysirg" then print "One",
if the string is a part of "education” then print "Two" and
if the string is a part of "services" then print "Three"."""
#solution 1
a=int(input("enter any number = "))
if a//1000==0:
   if a//100!=0:
       if a//10!=0:
        print("it is a three digit number")
       else:
        print("it is not a three digit number") 
   else:
        print("it is not a three digit number")
      
else:
    print("it is not a three digit number")
#solution 2
b=int(input("enter any number = "))
if b>0:
   print("positive")
elif b<0:
   print("negative")
else:
   print("zero")
#solution 3
a=int(input("enter\n1 for even-odd\n2 for positivw non-positive\n3 for simple interest\n4 for roots"))
if a==1:
  c=int(input("enter any number = "))
  while c%2==0:
    print("even")
    break
  while c%2!=0:
       print("odd")
       break
elif a==2:
   a=int(input("enter any number = "))
   while a>0:
     print("positive")
     break
   while a<=0:
       print("non-positive")
       break
elif a==3:
 p=int(input("enter principle"))
 t=int(input(" enter time"))
 r=int(input("enter rate"))
 print("simple interesr =",p*t*r/100)
else:
   #AX^2+BX+C
 A=a=int(input("enter A = "))
 B=int(input("enter B = "))
 C=int(input("C = "))
 if B**2-4*A*C==0:
   print("real and equal roots")
 elif B**2-4*A*C>0:
   print("real and distinct roots")
 else:
   print("imaginary roots")
#solution 4
k=eval(input("enter data"))
match k:
   case k if type(k)==int:
      print("monday")
   case k if type(k)==float:
      print("tuesday")
   case k if type(k)==complex :
      print("wednesday") 
   case k if type(k)==bool:
      print("thrusday")

#solution 5
b=input("enter a string")
match b :
   case b if b in'mysirg':
      print("one")
   case b if b in 'education':
      print("two")
   case b if b in 'services' :
      print("three") 


