#Relational operators:"==,!=,>=,<=,>,<"
#programs
#All relational operators using user input
a=int(input("Enter a number1:")) #7
b=int(input("Enter a number2:")) #2
print(a==b) #False
print(a!=b) #True
print(a>b)  #True
print(a<b)  #False
print(a>=b) #True
print(a<=b) #False

#check pass or fail
m=int(input("Enter marks:"))#30
if m>=14: #True
    print("pass") #pass
else:
    print("fail")

#compare three numbers
a=3
b=3
c=9
print(a==b==c)#False
print(a==b!=c)#True
print(a>b>c)#False
print(a<b<c)#False
print(a<=b<c)#True
print(c>b>=a)#True

#Grade eligibility check
a=int(input("Enter marks:"))
if a>=90:
    print("A grade")
elif a>=75:
    print("B grade")
else:
    print("C grade")

#compare len of strings
a="346"
b="hlo123"
print(len(a)<len(b)) #3<6#True

#relational operators with typecasting
x=float(input("Enter num:"))#34
y=float(input("Enter num:"))#34.4
print(int(x)==int(y))#True

#Alphabetical order check
ch1=input("Enter string:")#f
ch2=input("Enter string:")#g
print(ch1<ch2)#True

#what is the output?
print(10==10.0)#True
#Values are same, type doesn’t matter for ==

#compare int and str
print(10=="10")#False