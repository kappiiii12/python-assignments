"""
1. Write a python script to create a list of first N even natural numbers
2. Write a Python script to create a list of first N terms of a Fibonacci series
3. Write a Python script to create a list of first N prime numbers.
4. Write a Python script to add two matrices each of order 3 x 3. Store matrix elements in a list of lists.
5. Write a Python script to create two lists from a given list of numbers in such a way
   that the first list can have only positive numbers and second list can have only non
   positive numbers."""
#solution 1
n=int(input("enter the value of n = "))
l=[]
i=1
while i<=n:
    l.append(i)
    i+=1
print("list of first n natural numbers = ",l)
#solution 2
a=0
b=1
j=1
l2=[]
while j<=n:
    c=a+b
    l2.append(c)
    a=b
    b=c
    j+=1
print("list of n terms of febonacci = ",l2)
#solution 3
l3=[]
p=2
while n:
   for x in  range(2,p):
    if p%x==0:
       break
   else:
    l3.append(p)
    n-=1
   p+=1
print(l3)
#solution 4
print("Enter 9 elements of first matrix (row wise)")
A=[
    [int(s) for s in input().split(',')],
    [int(s) for s in input().split(',')],
    [int(s) for s in input().split(',')]
]
print("Enter 9 elements of second matrix (row wise)")
B=[
    [int(s) for s in input().split(',')],
    [int(s) for s in input().split(',')],
    [int(s) for s in input().split(',')]
]
C=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        C[i][j]=A[i][j]+B[i][j]
        print(C[i][j],end=' ')
    
#solution 5
l5=[1,2,3,4,5,-9,-8,-7,-7,0,5]
l6=[]
l7=[]
for x in l5:
   if x>0:
      l6.append(x)
   else:
      l7.append(x)
      
print(l6,l7)
