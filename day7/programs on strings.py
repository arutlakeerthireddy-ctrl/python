#1.find length of string
s=input("Enter a string: ")
print(len(s))  
#output: Enter a string: Hello
#5

#2.reverse a string
s=input("Enter a string: ")
print(s[::-1])
#output: Enter a string: Hello
#olleH

#3.check palindrome
s=input("Enter a string: ")
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
#output: Enter a string: madam
#Palindrome

#4.count vowels in a string
s=input("Enter a string: ")
vowels="aeiouAEIOU"
count=0
for char in s:
    if char in vowels:
        count+=1
print(count)
#output: Enter a string: Hello World
#3

#5.count consonants in a string
s=input("Enter a string: ")
vowels="aeiouAEIOU"
count=0
for ch in s:
    if ch.isalpha() and ch not in vowels:
        count+=1
print(count)
#output: Enter a string: Hello World
#7

#6.count digits in a string
s=input("Enter a string: ")
count=0
for ch in s:
    if ch.isdigit():
        count+=1
print(count)
"""output: Enter a string: Hello123World
3"""

#7.count words in a string
s=input("Enter a string: ")
print(len(s.split()))
"""output: Enter a string: Hello World from Python
4"""

#8.converts string to uppercase
s=input("Enter a string: ")
print(s.upper())
"""output: Enter a string: hello world
HELLO WORLD"""

#9.converts string to lowercase
s=input("Enter a string: ")
print(s.lower())
"""output: Enter a string: HELLO WORLD
hello world"""

#10.replace a substring in a string
s=input("Enter a string: ")
s1=input("Enter substring to replace: ")
s2=input("Enter replacement substring: ")
print(s.replace(s1,s2))
"""output: Enter a string: Hello World
Enter substring to replace:
World
Enter replacement substring:
Universe
Hello Universe"""

#11.check substring presence
s=input("Enter a string: ")
s1=input("Enter substring:")
if s1 in s:
    print("Substring found")
else:
    print("Substring not found")
"""output: Enter a string: Hello World
Enter substring:World
Substring found"""

#12.remove spaces from a string
s=input("Enter a string: ")
print(s.strip())
print(s.lstrip())
print(s.rstrip())
"""output: Enter a string:    Hello World
Hello World"""

#13.check anagrams
s1=input("Enter first string: ")
s2=input("Enter second string: ")
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")
"""output: Enter first string: listen
Enter second string: silent
Anagrams
"""
   

