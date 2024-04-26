"""
1. Write a python script to print first N even natural numbers.

2. Write a python script to print first N odd natural numbers

3. Write a python script to print squares of first N natural numbers.

4. Write a python script to print cubes of first N natural numbers.

5. Write a python script to display all prime numbers within a range. # range start = 15 end = 45"""
#solution 1
for e in range(1,int(input("enter the value of n"))+1) :
 print(2*e)
#solution 2
for e in range(1,int(input("enter the value of n"))+1) :
 print(2*e-1)
#solution 3
for e in range(1,int(input("enter the value of n"))+1) :
 print(e**2)
 #solution 4
for e in range(1,int(input("enter the value of n"))+1) :
 print(e**3)
#solution 5
start = int(input("enter starting value"))
end = int(input("end starting value"))

for x in range(start,end):
 for y in range(2,x):
   if x%y==0:
      break
 else:
   print(x)

  


    