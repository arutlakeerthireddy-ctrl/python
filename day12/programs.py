#Write a program to multiply a number by 2 using bitwise operator.
n=int(input("Enter number:"))#4
result=n<<1 #4<<1=4*2**1
print(result)#8

#multiply by 4,8,16
result=n<<2 #4<<2=4*2**2=16
result=n<<3 #4<<3=4*2**3=32
reslut=n<<4 #4<<4=4*2**4=64

#Write a program to divide a number by 4 using bitwise operator.
n=int(input("Enter number:"))#8
result=n>>2 #8>>2=8//2**2=2
print(result)#2

#Write a program to swap two numbers without using a temporary variable (using bitwise operator).
num1=int(input("Enter number:"))#4
num2=int(input("Enter number:"))#6
num1=num1^num2 #num1=4^6=100^110=010=2
num2=num1^num2 #num2=2^6=010^110=100=4
num1=num1^num2 #num1=2^4=010^100=110=6
print("num1=",num1)#6
print("num2=",num2)#4

