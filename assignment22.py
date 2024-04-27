"""
1. Write a Python script to calculate sum of first n natural numbers.

2. Write a Python script to calculate sum of squares of first N natural numbers

3. Write a Python script to calculate sum of cubes of first N natural numbers

4. Write a Python script to calculate sum of first N odd natural numbers.

5.Write a Python script to calculate sum of first n even natural numbers."""
#solution 1
sum=0
sqsum=0
cubesum=0
oddsum=0
evensum=0
for e in range(1,int(input("enter the value of n"))+1):
    sum+=e
    sqsum+=(e**2)
    cubesum+=(e**3)
    oddsum+=2*e-1
    evensum+=2*e

print("sum = ",sum)
#solution 2
print("sum of squares =",sqsum)
#solution 3
print("sum od cubes =",cubesum)
#solution 4
print("sum of first odds =",oddsum)
#solution 5
print("sum of first evens =",evensum)


