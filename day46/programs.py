#Write a program that takes user input repeatedly and stops when the user enters 0 using break.
while True:
    n=int(input("Enter number:"))
    if n==0:
        break
    print(n)


#Write a program to print all positive numbers from a list while skipping negative numbers using continue.
li=[1,-2,4,-6,-3,-2]
for num in li:
    if num<0:
        continue
    print(num)
        
        

