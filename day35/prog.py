#Write a program to count the number of vowels in a string.
str=input("Enter string:")
str.lower()
count=0
for i in str:
    if i in "aeiou":
        count+=1
print(count)

#Write a program to print numbers divisible by 3 between 1 and 50.

for i in range(1,51):
    if i%3==0:
        print(i)