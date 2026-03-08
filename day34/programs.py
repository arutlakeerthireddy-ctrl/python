#Write a program to find the sum of numbers from 1 to n.
n=int(input("Enter number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#Write a program to print the multiplication table of a given number.
num=int(input("Enter number:"))
for i in range(1,11):
    print(num,'x',i,"=",num*i)



 