#using different types of variables
name="keerthi"
age=20
height=5.6
print("Name:",name)
print("Age:",age)
print("Height:",height)

#Taking input and storing in a variable
name=input("Enter your name:")
print("Hello,",name)

#Adding two numbers using variables
a=10
b=20
sum=a+b
print(sum)

#swaping two variables
x=5
y=10
x,y=y,x
print(x,y)

#using global and local variables
x=10
def show():
    y=5
    print("Local variable y:",y)
show()
print("Global variable x:",x)
