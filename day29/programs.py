#Write a program to check whether a number is positive, negative, or zero. If positive, check whether it is even or odd.
num=int(input("Enter number:"))
if num>0:
    if num%2==0:
        print("number is positive and even")
    else:
        print("number is positive and odd")
elif num<0:
    print("number is negative")
else:
    print("number is zero")


#Write a program to check whether a year is a leap year. If it is a leap year, check whether it is divisible by 400.
num=int(input("Enter year: "))
if num%4==0:
    print("it is leap year")
    if num%400:
        print("it is divisible by 400")
    else:
        print("it is not divisible")
else:
    print("it is not leap year")
