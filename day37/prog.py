#Write a program to count the number of digits in a given number using a while loop.
n=int(input("Enter number:"))
count=0
while n>0:
    n=n//10
    count+=1
print(count)


#Write a program to reverse a given number using a while loop.
n=int(input("Enter number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)


#Write a program to check whether a number is a palindrome using a while loop.
n=int(input("Enter number:"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
        print("palindrome")

