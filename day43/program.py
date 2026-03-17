#Write a program to check whether a number is prime using a nested loop.
n=int(input("Enter number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
for j in range(1):
    if count==2:
        print("prime number")
    else:
        print("not prime number")
