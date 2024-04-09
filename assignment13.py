"""
1. Write a python script to check whether a given number is a three digit number or not.

2. Write a python script to check whether a given number is positive, negative or zero.

3. Write a python script to check whether 
a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots

4. Write a python script to check whether a given year is a leap year or not.

5. Write a python script to print greater among three numbers. 
Print number only once even if the numbers are the same."""
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
Y=int(input("enter the year"))
if Y%4==0 :
   if Y%100==0:
      if Y%400==0:
         print("leap year")
      else: 
         print("not a leap year")
   else:
    print("leap year")
else:
   print("nt a leap year")
#solution 5
a=int(input("enter any number = "))
b=int(input("enter any number = "))
c=int(input("enter any number = "))
if a>b and a>c:
   print(a,"is greater")
elif b>a and b>c:
   print(b,"is greater")
else:
   print(c,"is greater")
   
   



         

         
      
    