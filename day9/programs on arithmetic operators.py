#Arithmetic  operators:+,-,*,/,%,//,**
#programs 
#1.All arithmetic operations using user input
"""x=int(input("Enter a num1:"))
y=int(input("Enter a num2:"))
print("Addition:",x+y)
print("Subtraction:",x-y)
print("Multiplication:",x*y)
print("Division:",x/y)
print("modulus:",x%y)
print("Floor division:",x//y)
print("power:",x**y)

#2.swap two numbers using arithmetic operators
x=int(input("Enter a num1:"))
y=int(input("Enter a num2:"))
x=x+y
y=x-y
x=x-y
print("x=",x)
print("y=",y)

#3.simple calculator using arithmetic operators
a=int(input("Enter a num1:")) #5
b=int(input("Enter a num2:")) #4

cal=input("Arithmetic operators:") #+,-,*,/,%,//,**
if cal == "+": #True
   print("Add:",a+b) #5+4=9
elif cal == "-":
   print("Sub:",a-b) #5-4=1
elif cal == "*": 
   print("mul:",a*b) #5*4=20
elif cal == "/":
   print("div:",a/b) #5/4=1.2
elif cal == "%":
   print("mod:",a%b) #5%4=1
elif cal == "//":
   print("floor div:",a//b) #5//4=1
else:
   print("power:",a**b) #5**4=625

#4.Area of a rectangle
l=10
b=5
a=l*b
print("Area of rectangle:",a)

#5.Average of three numbers
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))
avg=(num1+num2+num3)/3
print("Average of three numbers:",avg)

#6.calculate total and percentage
m1=80
m2=96
m3=92
total=m1+m2+m3
percent=(total/300)*100
print("Total:",total)
print("Percentage:",percent)

#7 square and cube of a number
n=3
print("square:",n**2)
print("cube:",n**3)"""

#8.Adding length of strings using arithmetic 
s1="python"
s2="program"
print(len(s1)+len(s2))
