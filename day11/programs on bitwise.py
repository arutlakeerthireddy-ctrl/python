#Write a program to perform bitwise AND of two numbers.
"""a=int(input("Enter num1:"))#1=01
b=int(input("Enter num2:"))#5=101
print(a&b)#1=01

#Write a program to perform bitwise OR of two numbers.
a=int(input("Enter num1:"))#6=110
b=int(input("Enter num2:"))#3=011
print(a|b)#7=111

#Write a program to perform bitwise XOR of two integers.
a=int(input("Enter num1:"))#6=110
b=int(input("Enter num2:"))#3=011
print(a^b)#5=101

#Write a program to find bitwise NOT of a number.
a=int(input("Enter num1:"))#9=1001
print(~a)#~n=-(n+1)=-10

#Write a program to perform left shift by given positions.
x=int(input("Enter number:"))#4=100
n=int(input("Enter no. of left shifts:"))#1
print(x<<n)#x<<n=x*(n**2)=4*(1**2)=8

#Write a program to perform right shift by given positions.
x=int(input("Enter the number:"))#7
n=int(input("Enter no. of right shifts:"))#2
print(x>>n)#x>>n=x//(n**2)=1"""

#Write a program to check whether a number is even or odd using bitwise operators.
n=int(input("Enter number:"))
if n&1==0:
    print("even")
else:
    print("odd")
