#what is string in python?
string is a text datatype 
it is a sequence of characters(letters,digits,symbols,spaces)enclosed in a quotes.
strings can be written in single quotes('')
                          double quotes("")
                          triple quotes(""" """)/(''' ''')
string is immutable(we cannot change the characters of a string once it is created)
#example:
name='keerthi'
course="python"
description='''python is a programming language'''

#string operations:
string operations are used manipulate,compare and work with text data.
some common string operations are:

#1.concatenation
join two or more strings together using + operator.
#example:
a='hello'
b='world'
c=a+" "+b
print(c) #hello world

#2.repetition
repeat a string multiple times using * operator.
#example:
a="keerthi "
b=a*3
print(b) #keerthi keerthi keerthi

#3.indexing
Access characters in a string using index
#indexing starts from 0 for the first character
1.positive indexing(from left to right)
2.negative indexing(from right to left)
#example:
s="python"
print(s[0])#p
print(s[3])#h
print(s[-1])#n

#4.slicing
Extract a substring from a string 
using the slice notation[start:end:step]
#example:
   #1.positive slicing
   s="keerthi"
   print(s[0:5])#keert

   #2.slicing with missing index
   print(s[2:])#erthi
   print(s[:4])#keer

   #3.negative slicing
   print(s[-6:-1])#eerth

   #4.slicing with step
   print(s[0:7:2])#krti

   #5.reverse slicing
   print(s[::-1])#ihtreek

#5.length
finds the number of characters in a string using len() function.
#example:
s="python"
print(len(s))#6

#6.membership
check if a substring exists in a string using in and not in operators.
#example:
s="keerthi reddy"
print("ke" in s) #True
print("arutla" in s) #False" 
print("reddy" not in s) #False

#7.comparison
compare two strings using comparison operators(==,!=,<,>,<=,>=)
#example:
print("apple"=="apple") #True
print("mango"!="apple") #True
print("mango"<"apple") #False
print("mango">"apple") #True
print("mango"<="apple") #False
print("mango">="apple") #True

#8.iteration
loop through each character in a string using for loop.
#example:
for i in "keerthi":
    print(i)
#k
#e
#e
#r
#t
#h
#i

#9.string formatting
insert values into a string using format() method or f-strings.
#example:
name="keerthi"
print(f'hello,{name}!')#hello,keerthi!













    
