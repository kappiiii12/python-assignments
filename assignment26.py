"""
1.Write a python script to check if a given string has only alphabets in it.
2.Write a python script to check if a given character is present in a given string or not.
3.Write a python script to count vowels in a given string.
4. Write a python script to reverse a string
5.Write a python script to count words in a given string
"""
#solution 1
alphabet="kapil"
k=alphabet.isalpha()
print(k)
#solution 2
p= "ka" in alphabet
print(p)
#solution 3
l=alphabet.count('a')
l+=alphabet.count('e')
l+=alphabet.count('i')
l+=alphabet.count('o')
l+=alphabet.count('u')
print(l)
#solution 4
k=alphabet[::-1]
print(k)
#solution 5
m=len(alphabet)
print(m)