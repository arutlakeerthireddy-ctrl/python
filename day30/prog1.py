#Write a program to check whether a number is a multiple of both 3 and 7.
num=int(input("Enter number:"))
if num%3==0 and num%7==0:
    print("multiple")
else:
    print("not")