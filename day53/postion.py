#position arguments:
#arguments are values that are passed to function  based on postion(correct order)
#example
def add(a,b):
    return a+b
print(add(2,3)) #5
print(add(3,2))  #wrong

def greet(name,age):
    print(name,age)#keerthi 21
greet("keerthi",21)
greet(21,"keerthi") #21,"keerthi" wrong meaning

def multiply(a,b,c):
    print(a*b*c)#24
multiply(2,3,4)

def square(n):
    print(n*n)#25
square(5)

def memo(name,roll,marks,percent):
    print(name,roll,marks,percent) #keerthi 14 95 90
memo("keerthi",14,95,90)
memo(1,2,3,4) #1,2,3,4 wrong meaning
    