"""
1. Write a python script to print the first 10 multiples of 5.

2. Write a python script to print first 10 multiples of N

3. Write a python script to print first M multiples of N.

4. Write a python script to print the first 10 multiples of N in reverse order.

5. Write a python script to print table of user's choice"""
    
#solution 1
for e in range(1,11) :
    print(5*e)
#solution 2
n=int(input("enter the value of N"))
for e in range(1,11) :
    print(n*e)
#solution 3
n=int(input("enter the value of n"))
m=int(input("enter the value of m"))
for e in range(1,m+1) :
    print(n*e)
#solution 4
n=int(input("enter the value of N"))
for e in range(10,0,-1) :
    print(n*e)
#solution 5
n=int(input("enter the value of N"))
for e in range(1,11) :
    print(n ,"*", e ,"=" ,n*e)
