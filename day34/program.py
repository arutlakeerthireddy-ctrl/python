#Write a program to find the factorial of a number using a for loop.
n=int(input("Enter number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial",fact)


#Write a program to print numbers in reverse from 10 to 1.
for i in range(10,0,-1):
    print(i)

#Write a program to print the square of numbers from 1 to 10.
for i in range(1,11):
    square=i*i
    print(square)


