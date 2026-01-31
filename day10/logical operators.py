#logical operators:used to combine conditional statements
#and:True if both conditions are true
#or:True if atleast one condition is true
#not:reverse the result
#programs

#1.Write a program to check whether a number is positive and even.
a=int(input("Enter a number:"))
print(a>0 and a%2==0)

#2.Write a program to check whether a number is negative or zero.
num=int(input("Enter a number:"))
print(num<0 or num==0)

#3.Write a program to check whether a number lies between 10 and 100.
num=int(input("Enter a number:"))
print(10<num and num<100)

#4.Write a program to check if a student passes when either theory or practical marks are ≥ 35.
a=int(input("Enter theory marks:"))
b=int(input("Enter practical marks:"))
print(a>=35 or b>=35)

#5.Write a program to validate username and password using logical operators.
a=input("Enter username:")#keerthi
b=input("Enter passwords:")#9014
print(a=="keerthi" and b=="9014")#True

#6.Write a program to check if a year is leap year using logical operators.
y=int(input("Enter year:"))#2024
print(y%4==0 and y%100!=0 or y%400==0)#True

#7.Write a program to check if a character is a vowel or consonant.
ch=input("Enter a character:")
v="a,e,i,o,u"
print(ch in v or ch not in v )

#8.Write a program to check whether a number is divisible by 3 and 5.
num=int(input("Enter number:"))#30
print(num%3==0 and num%5==0)#True

#9.Write a program to check whether a person is eligible for senior citizen benefits (age ≥ 60 and not working).
age=int(input("Enter person age:"))#70
working=input("Enter senior citizen working:")#no
print(age>=60 and working=="no")#True

#10.NOT operator
is_raining=True
print(not is_raining)#False"""