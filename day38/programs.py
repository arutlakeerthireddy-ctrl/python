#Write a program to find the factorial of a number using a while loop.
n=int(input("Enter number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact)

#Write a program to print the Fibonacci series up to n terms using a while loop.
n=int(input("Enter no. of terms:"))
a=0
b=1
i=1
while i<=n:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1


