#Write a program to find the largest digit in a number using a while loop.
n=int(input("Enter number:"))
li=[]
while n>0:
    digit=n%10
    li.append(digit)
    n=n//10
print(max(li))

#without using list
n=int(input("Enter number:"))
max=0
while n>0:
    digit=n%10
    if digit>max:
        max=digit
    n=n//10
print(max)


#Write a program to calculate the product of digits of a number using a while loop.
n=int(input("Enter number:"))
product=1
while n>0:
    digit=n%10
    product*=digit
    n=n//10
print(product)

