#check largest of three numbers
a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))
if a>b:
    if a>c:
        print("largest number :",a)
    else:
        print("largest number:",c)
else:
    if b>c:
        print("largest number is :",b)
    else:
        print("largest number is :",c)
    
