#Write a program to check whether a character is uppercase or lowercase.
ch=input("Enter character:")
ch1=ch.lower()
if ch in ch1:
    print("character is lowercase")
else:
    print("uppercase")

#Write a program to check whether a number is a 3-digit palindrome (e.g., 121).
num=input("Enter number:")
if num==num[::-1] and len(num)==3:
    print("3 digit palindrome")
else:
    print("not")

#Write a program to check whether three sides can form a right-angled triangle.
a=2
b=3
c=5
if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
    print("right angled triangle")
else:
    print("not")
