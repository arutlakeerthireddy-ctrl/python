#Write a program to print all odd numbers from 1 to 50 using a while loop.
i=1
while i<=50:
    print(i)
    i+=2

#Write a program to find the sum of numbers from 1 to n using a while loop.
n=int(input("Enter number:"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print(sum)

#Write a program to print the multiplication table of a number using a while loop.
num=int(input("Enter number:"))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1