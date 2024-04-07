"""
1. Write a python script to remove the last digit from a given number. 
(for example, if user enters 2534 then your output should be 253 )

2. Write a python script to get the last digit from a given number. 
(for example, if user enters 2089 then your output should be 9)

3. Write a python script to swap data of two variables

4. Write a python script which takes a three digit number from the user and displays only its first digit.

5. Write a python script which takes a three digit number from the user and displays only its middle digit."""
#solution 1
a=int(input("enter any nymber = "))
print(a//10)
#solution 2
a=int(input("enter any nymber = "))
print(a%10)
#solution 3
a=int(input("a = "))
b=int(input("b = "))
a=a+b
b=a-b
a=a-b
print("a = ",a,"b = ",b)
#solution 4
a=int(input("enter a three digit nymber = "))
print(a//100)
#solution 5
a=int(input("enter a three digit nymber = "))
print((a//10)%10)
