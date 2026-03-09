#Write a program to find the largest number in a list using a for loop.
li=[1,4,5,2,8]
largest=li[0]
for i in li:
    if i>largest:
        largest=i
print(largest)#8


#Write a program to print each character of a string using a for loop.
str=input("Enter string:")
for i in str:
    print(i)
