#Write a program to check whether a number is greater than 100. 
#If yes, check whether it is a multiple of 10.
num=int(input("Enter number:"))
if num>100:
    print("greater than 100")
    if num%10==0:
        print("multiple of 10")
    else:
        print("not")