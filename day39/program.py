#Write a program to find the sum of even numbers between 1 and n using a while loop.

n=int(input("Enter number:"))
i=2
sum=0
while i<=n:
    if i%2==0:
        sum+=i
        i+=2
print(sum)

#Write a program to print squares of numbers from 1 to 10 using a while loop.

i=1
while i<=10:
    print(i**i)
    i+=1
