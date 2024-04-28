"""
1. Write a Python script to calculate factorial of a given number.
2. Write a Python script to count digits in a given number.
3. Write a Python script to calculate sum of digits of a given number.
4. Write a Python script to print binary equivalent of a given decimal number. (Do not use bin() method)
5. Write a Python script to print the octal equivalent of a given decimal number. (Do notuse oct() method)
"""
#solution 1
b=1
for e in range(1,int(input("enter any nymber"))+1):
    b*=e
print("factorial of given number is ",b)
#solution 2
a=int(input("enter any number"))
count=0
while a!=0:
    a//=10
    count+=1
print("digits in given number =",count)
#solution 3
k=int(input("enter any number"))
x=0
while k!=0:
    a=a+k%10
    k=k//10
print("sum of digits of given number =",a)
#solution 4
d=int(input("enter any number"))
s=''
while d:
    s=str(d%2)+s
    d//=2
print(s)
#solution 5
l=int(input("enter any number"))
m=''
while l:
    m=str(l%8)+m
    l//=8
print(m)

