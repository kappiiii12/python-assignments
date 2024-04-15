"""
1. Write a python script to check whether a given number is positive or non-positive

2. Write a python script to check whether a given number is divisible by 5 or not

3. Write a python script to check whether a given number is even or odd

4. Write a python script to print greater between two numbers.
 Print number only once even if the numbers are the same.

5. Write a python script to print two given words in dictionary order"""
#solution 1
a=int(input("enter any number = "))
while a>0:
    print("positive")
    break
while a<=0:
       print("non-positive")
       break

#solution 2
b=int(input("enter any number = "))
while b%5==0:
    print("divisible by 5")
    break
while b%5!=0:
       print("non-divisible by 5")
       break
#solution 3
c=int(input("enter any number = "))
while c%2==0:
    print("even")
    break
while c%2!=0:
       print("odd")
       break
#solution 4
d=int(input("enter any number = "))
e=int(input("enter any number = "))
while d>=e:
      print(d,"is greater")
      break
while d<e:
      print(e,"is greater")
      break
#solution 5
f=input("enter a string")
g=input("enter another string")
if f>g:
      print(g,f,sep='\n')
else:
      print(f,g,sep='\n')


 