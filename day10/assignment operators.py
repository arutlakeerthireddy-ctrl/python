#Assignment operators are used to assign or update values in a variable
#operators:=,+=,-=,*=,/=,%=,//=,**=
#programs
#1.Write a program to increase a number by 10 using +=.
"""num=int(input("Enter number:"))
num+=10
print(num)

#2.Write a program to decrease a value by 5 using -=.
num=int(input("Enter a number:"))
num-=5
print(num)

#3.Write a program to multiply a number by 3 using *=.
num=int(input("Enter a number:"))
num*=3
print(num)

#4.Write a program to divide a number by 2 using /=.
num=int(input("Enter number:"))
num/=2
print(num)

#5.Write a program to find remainder using %= operator.
num=int(input("Enter number:"))
num%=10
print(num)

#6.Write a program to calculate power of a number using **=.
num=int(input("Enter number:"))
num**=6
print(num)

#7.Write a program to sum first N natural numbers using assignment operator.
n=int(input("Enter no. of numbers"))
n+=1
n/=2
n*=n
print(n)

#8.Write a program to reverse a number using assignment operators.
num=input("Enter number:")
rev=""
rev+=num[::-1]
print(rev)

#9.Write a program to update bank balance after withdrawal.
a=int(input("Enter bank balance:"))
b=int(input("Enter withdraw amount:"))
a-=b
print(a)

#10.Write a program to update salary after increment.
s=int(input("Enter initial salary:"))
i=int(input("Enter increment:"))
s+=i
print(s)"""

#11.Write a program to calculate total bill amount after discount.
amount=int(input("Enter bill amount:"))
dis=float(input("Enter discount:"))
total=amount*dis/100
amount-=total
print("total:",amount)

