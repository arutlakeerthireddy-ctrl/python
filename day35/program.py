# Program to print Fibonacci series up to n terms

n=int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


#Write a program to check whether a number is prime using a for loop.
n=int(input("Enter number:"))
count=0
for i in range(1,n+1):
    if n % i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not a prime number")
    