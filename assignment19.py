"""
1. Write a python script to print each character of a string with its corresponding Unicode.

2. Write a Python script to print only vowels of the given string

3. Write a Python script to count occurrence of spaces in a given string.

4. Write a Python script to print unique digits of a given integer.

5. Write a Python script to count number of digits in a given number."""
#solution 1
a=input("enter any string")
for x in a:
    print(x,ord(x))
#solution 2
for x in a:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' :
        print(x)
#solution 3
count=0
for x in a:
    if x==' ':
        count+=1
print(count)
#solution 4
b=input("enter a number")
i=0
for k in b:
    if b.index(k)==i:
      print(k,end='')
    i+=1  
#solution 5
b=input("enter a number")
i=0
for k in b:
    i+=1
print(i)

