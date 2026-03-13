#Write a program to print all numbers between 1 and 100 that are divisible by both 3 and 5 using a while loop.

i=1
while i<=100:
    if i%3==0 and i%5==0:
        print(i)
    i+=1


#Write a program to keep taking numbers from the user until the user enters 0 using a while loop.

n=int(input("Enter number:"))
while n!=0:
    print("you entered num:",n)
    n=int(input("Enter number:"))
    Enter number:5
    
"""you entered num: 5
Enter number:3
you entered num: 3
Enter number:0"""
    
    
