"""
1. Write a python script containing a variable with some integer value, print value of this variable.
2. Write a python script to print the value of a variable. Variable contains your name as data.
3. Write a python script to print values of three variables, each in a new line. 
All three variables are filled with some integer values.
4. Create 5 variables each of them containing different types of data (like 35, True, "MySirG", 5.46, 3+4j, etc). 
Write a python script to print values of all the variables along with their data types.
5. Create three variables and assign current date to them, first variable contains day number, 
second variable contains month number and third variable contains year number.
 Write a python script to display date in standard way (e.g. 29/11/2022)"""
# solution 1
a=4
print(a)
#solution 2
a='kapil'
print(a)
#solution 3
a,b,c=1,2,3
print(a,b,c,sep='\n')
#solution 4
a,b,c,d,e=35,True,"MYSIRF",5.46,3+4j
print( a,type(a))
print( b,type(b))
print( c,type(c))
print( d,type(d))
print( e,type(e))
#solution 5
a,b,c=29,11,2022
print(a,b,c,sep='/')
