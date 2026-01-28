# String Methods in Python
string methops are built in functions used to modify,search analyze strings.
they do not change the original string but return a new string.

some common string methods are:
#1.lower()
convert all characters in a string to lowercase.
#example:
print("HELLO WORLD".lower()) #hello world

#2.upper()
convert all characters in a string to uppercase.
#example:
print("hello world".upper()) #HELLO WORLD

#3.title()
convert the first character of each word to uppercase.
#example:
print("hello world from python".title()) #Hello World From Python

#4.capitalize()
convert the first character of the string to uppercase.
#example:
print("hello world".capitalize()) #Hello world

#5.swapcase()
swaps uppercase characters to lowercase and vice versa.
#example:
print("Hello World".swapcase()) #hELLO wORLD

#6.isalpha()
check if all characters in the string are alphabetic.
#example:
print("Hello".isalpha()) #True
print("Hello123".isalpha()) #False

#7.isdigit()
check if all characters in the string are digits.
#example:
print("12345".isdigit()) #True
print("123abc".isdigit()) #False

#8.isalnum()
check if all characters in the string are alphanumeric.
#example:
print("Hello123".isalnum()) #True
print("Hello@123".isalnum()) #False

#9.islower()
check if all characters in the string are lowercase.
#example:
print("hello".islower()) #True
print("Hello".islower()) #False

#10.isupper()
check if all characters in the string are uppercase.
#example:
print("WORLD".isupper()) #True
print("World".isupper()) #False

#11.istitle()
check if the string is in title case.
#example:
print("Hello World".istitle()) #True
print("hello world".istitle()) #False

#12.isspace()
check if all characters in the string are whitespace.
#example:
print("   ".isspace()) #True
print("  a  ".isspace()) #False

#13.find()
returns the first occurrence index of a substring in the string. returns -1 if not found.
#example:
print("hello world".find("world")) #6
print("hello world".find("python")) #-1
print("hello world".find("o")) #4

#14.rfind()
returns the last occurrence index of a substring in the string. returns -1 if not found.
#example:
print("hello world".rfind("o")) #7
print("hello world".rfind("python")) #-1

#15.index()
returns the first occurrence index of a substring in the string. raises ValueError if not found.
#example:
print("hello world".index("world")) #6
print("hello world".index("keerthi")) #ValueError

#16.count()
counts the number of occurrences of a substring in the string.
#example:
print("hello world".count("o")) #2
print("hello world".count("l")) #3

#17.startswith()
checks if the string starts with a given value.
#example:
print("hello world".startswith("hello")) #True
print("hello world".startswith("world")) #False

#18.endswith()
checks if the string ends with a given value.
#example:
print("hello world".endswith("world")) #True
print("hello world".endswith("hello")) #False

#19.replace()
replace old value with new value in the string.
#example:
print("hello world".replace('world','keerthi')) #hello keerthi
print("hello world".replace('l','0')) #he00o wor0d

#20.split()
split string into a list
#example:
print("hi iam keerthi".split()) #['hi','iam','keerthi']
print("a,b,c,d".split(',')) #['a','b','c','d']

#21.join()
join elements using a seperator
#example:
print("-".join(["2024","06","15"])) #2024-06-15
print(" ".join(["hello","world"])) #hello world

#22.strip()
remove spaces from both ends of the string.
#example:
print("  keerthi  ".strip()) #'keerthi'

#23.lstrip()
remove spaces from the left end of the string.
#example:
print("  keerthi  ".lstrip()) #'keerthi  '

#24.rstrip()
remove spaces from the right end of the string.
#example:
print("  keerthi  ".rstrip()) #'  keerthi'

#25.center()
center the string within a specified width.
#example:
print("keerthi".center(20,'*')) #******keerthi*******
print("hello".center(10,"-")) #--hello---

#26.ljust()
left align the string within a specified width.
#example:
print("keerthi".ljust(15,'-')) #keerthi--------
print("hello".ljust(10,'*')) #hello*****

#27.rjust()
right align the string within a specified width.
#example:
print("keerthi".rjust(15,'-')) #--------keerthi
print("hello".rjust(10,'*')) #*****hello

#28.zfill()
pad the string with zeros on the left to fill a specified width.
#example:
print("42".zfill(5)) #00042 
print("keerthi".zfill(10)) #000keerthi

#29.partition()
split the string into 3 parts using a separator.
#example:
print("hello python world iam keerthi".partition("world")) #('hello python ', 'world', ' iam keerthi')
print("keerthi-reddy".partition("-")) #('keerthi', '-', 'reddy')

#30.rpartition()
split the string into 3 parts using a separator from the right.
#example:
print("hello python world iam keerthi".rpartition("world")) #('hello python ', 'world', ' iam keerthi')
print("keerthi-reddy".rpartition("-")) #('keerthi', '-', 'reddy')

#31.encode()
encode the string into bytes using a specified encoding.
#example:
print("keerthi".encode('utf-8')) #b'keerthi'

#32.format()
formats string with values.
#example:
name="keerthi"
age=21
print("my name is {} and i am {} years old".format(name,age)) #my name is keerthi and i am 21 years old

#33.format_map()
formats string using a dictionary.
#example:
data={'name':'keerthi','age':21}
print("my name is {name} and i am {age} years old".format_map(data)) #my name is keerthi and i am 21 years old






