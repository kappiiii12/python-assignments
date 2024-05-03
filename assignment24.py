"""
1. Write a python script to calculate sum of elements of a list.

2. Write a Python script to calculate average of elements of a list.

3. Write a Python script to create a list of squares of numbers of a given list.

4. Write a Python script to sort list elements in descending order.

5. Write a Python script to create a list from a given list by selecting only even places
elements."""
#solution 1
l=[1,2,3,4,8,6]
s=0
i=0
for x in l:
    s+=x
    i+=1
print("sum =",s)
#solution 2
print("average =",s/i)
#solution 3
for x in l:
    print(x**2)
#solution 4
l.sort(reverse=True)
print(l)
#solution 5
l2=[]
i=0
for x in l:
    if i%2==0:
        l2.append(x)
    i+=1

print(l2)
    
