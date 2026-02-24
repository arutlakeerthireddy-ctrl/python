#Write a program to check whether a number is positive.
num=int(input("Enter number:"))
if num>0:
    print("number is positive")

# Write a program to check whether a number is negative.
num=int(input("Enter number:"))
if num<0:
    print("number is negative")

# Write a program to check whether a number is even.
num=int(input("Enter number:"))
if num%2==0:
    print("even")

# Write a program to check whether a number is divisible by 3.
num=int(input("Enter number:"))
if num%3==0:
    print("divisible by 3")

# Write a program to check whether a person is eligible to vote (age ≥ 18).
age=30
if age>=18:
    print("Eligible to vote")

# Write a program to check whether a student passed the exam (marks ≥ 35).
marks=50
if marks>=35:
    print("passed")

# Write a program to check whether a number is greater than 100.
num=100.1
if num>100:
    print("greater")

# Write a program to check whether a character is a vowel.
ch="e"
if ch in "aeiouAEIOU":
    print("vowel")

# Write a program to check whether a number is a multiple of 5.
num=10
if num%5==0:
    print("multiple of 5")

# Write a program to check whether a year is a leap year (use only if).
year=2020
if (year%400==0) or (year%4==0 and year%100!=0):
    print("leap year")