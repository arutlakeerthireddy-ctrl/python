#Write a program to count consonants in a string.
s=input("Enter string:")
s.lower()
count=0
for ch in s:
    if ch not in "aeiou":
        count+=1
print(count)


#Write a program to reverse a string using a for loop.
s=input("Enter string:")
for ch in s[::-1]:
    print(ch)

#Write a program to count the number of uppercase and lowercase letters in a string.
s=input("Enter string:")
upper_count=0
lower_count=0
for ch in s:
    if ch.isupper():
        upper_count+=1
    if ch.islower():
        lower_count+=1
print("uppercase:",upper_count)
print("lowercase:",lower_count)


#Write a program to calculate the sum of elements in a list.
li=list(map(int,input("Enter numbers:").split()))
sum=0
for i in li:
    sum+=i
print(sum)